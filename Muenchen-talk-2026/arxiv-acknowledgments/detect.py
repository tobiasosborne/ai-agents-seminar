#!/usr/bin/env python3
"""Step 3 -- find LLM mentions, and decide which ones are *acknowledgments*.

Three things must be kept apart, and the exercise is worthless if they are not:

  (a) the paper ACKNOWLEDGES LLM assistance         <- what we count
  (b) the paper is ABOUT LLMs                       <- counted separately, excluded
  (c) the paper explicitly DENIES using an LLM      <- counted separately, excluded
      ("no generative AI was used in preparing this manuscript")

(b) is decided from title+abstract.  (a) and (c) are decided from the full text.

Design note on recall.  An earlier version only looked inside a heading-delimited
"Acknowledgments" section and missed a third of the corpus: pdftotech renders
REVTeX headings as "V. ACKNOWLEDGMENTS", sometimes letter-spaced
("A c k n o w l e d g m e n t s"), often run-in ("Acknowledgements.-The authors
thank ..."), and plenty of papers have no heading at all, just a floating
"S.L. acknowledges support from ..." sentence.  So instead we scan the WHOLE
text for LLM terms and then ask, for each match, whether it sits in an
acknowledgment/disclosure CONTEXT -- either inside a heading-delimited region or
within a few hundred characters of an acknowledgment cue.  That keeps recall
high; precision is then bought back with (i) ambiguity rules for words like
"Claude" and "Gemini" that have innocent physics readings, and (ii) a by-hand
pass over every surviving snippet (results/hits.jsonl -> manual_overrides.json).

Outputs results/papers.csv (one row per sampled paper) and results/hits.jsonl.
"""

from __future__ import annotations

import csv
import gzip
import signal
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
LIST = ROOT / "data" / "listings"
TEXT = ROOT / "data" / "text"
RES = ROOT / "results"

# ---------------------------------------------------------------- normalising
# pdftotext emits letter-spaced headings for some font encodings.
SPACED_ACK = re.compile(
    r"(?i)\bA\s?c\s?k\s?n\s?o\s?w\s?l\s?e\s?d\s?g\s?e?\s?m\s?e\s?n\s?t\s?s?\b")


def normalise(text: str) -> str:
    return SPACED_ACK.sub("Acknowledgments", text)


# ---------------------------------------------------------------- ack regions
_ACKWORD = (r"acknowledge?ments?|"
            r"funding(?:\s+(?:information|statement))?|"
            r"author\s+contributions?|"
            r"(?:declaration|statement|disclosure)s?"
            r"(?:\s+(?:of|on|regarding))?(?:\s+the)?(?:\s+use\s+of)?"
            r"(?:\s+generative)?"
            r"\s+(?:ai|artificial\s+intelligence|llms?|interest)|"
            r"(?:generative\s+)?ai\s+(?:usage|use|assistance|tools?|statement|disclosure)|"
            r"use\s+of\s+(?:generative\s+)?(?:ai|llms?|large\s+language\s+models?)")

# A heading: start of line, optional section label (roman numeral / letter /
# digits), the word, optional trailing punctuation. Text may run on afterwards.
ACK_HEAD = re.compile(
    r"(?im)^[\W\d]{0,6}(?:[IVXLC]{1,6}[.)]?\s+|[A-Z][.)]\s+|\d+(?:\.\d+)*[.)]?\s+)?"
    r"(?:" + _ACKWORD + r")\b[\s.:*·—–-]{0,4}")

# Run-in form anywhere: "Acknowledgements.-The authors wish to thank ..."
ACK_INLINE = re.compile(
    r"(?i)\b(?:" + _ACKWORD + r")\b[\s.:*·—–-]{0,4}(?=[A-Z(])")

ACK_END = re.compile(
    r"(?im)^[\W\d]{0,8}(references|bibliography|appendix|supplement\w*|"
    r"notes?\s+and\s+references)\b|^\s*\[\s*1\s*\]\s")

ACK_WINDOW = 3000

# Cues that a sentence is doing acknowledgment / disclosure work, used when an
# LLM term is found OUTSIDE any heading-delimited region.
ACK_CUE = re.compile(
    r"(?i)(acknowledg|we\s+(?:thank|are\s+grateful|would\s+like\s+to\s+thank)|"
    r"the\s+authors?\s+(?:thank|are\s+grateful|wish\s+to\s+thank)|"
    r"grateful|declaration|disclos|"
    r"(?:was|were|has\s+been|have\s+been|is)\s+used\s+(?:to|for|in|only|solely|"
    r"exclusively|during|in\s+the)|"
    r"(?:we|the\s+authors?|i)\s+(?:used|use|have\s+used|employed|acknowledge)\b|"
    r"(?:polish|proofread|proof-read|improve|refine|edit|check|correct|assist)"
    r"\w*\s+(?:the\s+)?(?:english|language|grammar|wording|text|manuscript|"
    r"writing|readability|presentation|prose)|"
    r"(?:writing|preparation|editing|drafting|proofreading)\s+of\s+(?:this|the)\s+"
    r"(?:manuscript|paper|article|work|text)|"
    r"for\s+(?:help|assistance|support)\s+(?:with|in)|"
    r"assist\w*\s+(?:with|in|the)|"
    r"generative\s+ai|ai[\s-]assist)")

CUE_RADIUS = 420

# Where the bibliography starts.  Reference lists are a rich source of false
# positives ("Language models are few-shot learners", "Attention is all you
# need"), and an LLM term inside one is a citation, never an acknowledgment.
REFS_HEAD = re.compile(r"(?im)^[\W\d]{0,8}(references|bibliography)\b")
REFS_RUN = re.compile(r"\[\s*1\s*\]\s*[A-Z]")


def refs_start(text: str) -> int:
    """Best guess at where the reference list begins (len(text) if none)."""
    cands = [m.start() for m in REFS_HEAD.finditer(text)]
    # A numbered reference list: [1] ... [2] ... [3] within a short span.
    for m in REFS_RUN.finditer(text):
        i = m.start()
        tail = text[i:i + 6000]
        if "[2]" in tail and "[3]" in tail:
            cands.append(i)
            break
    # Take the LAST plausible start in the first pass, but never something in
    # the first third of the paper (that would be a forward reference).
    cands = [c for c in cands if c > 0.25 * len(text)]
    return min(cands) if cands else len(text)


# A match whose immediate neighbourhood looks like a bibliography entry is a
# citation, not an acknowledgment ("Flamingo: a visual language model", "Brown
# et al., Language models are few-shot learners").  This catches author-year
# reference lists, which refs_start() cannot delimit.
BIBLIO_CUE = re.compile(
    r"(?i)(et\s+al\.|doi\.org|\bdoi:|arxiv:|advances\s+in\s+neural|"
    r"proceedings\s+of|\bin\s+proc\.|preprint|\bpp\.\s*\d|"
    r"phys\.\s*rev\.|\bvol\.\s*\d|\(20[0-2]\d\)\.)")

# "GPT" in quant-ph overwhelmingly means *generalised probabilistic theory*.
GPT_PHYSICS = re.compile(
    r"(?i)\b(generali[sz]ed?\s+probabilistic|probabilistic\s+theor|"
    r"gpt\s+(?:system|theor|framework|state|model\s+of|formalism)|"
    r"(?:in|of|a|the)\s+gpts?\b|convex\s+operational)")

# ---------------------------------------------------------------- LLM patterns
STRONG = {
    "chatgpt":       r"(?i)chat\s?-?\s?gpt",
    "gpt-n":         r"(?i)\bgpt[\s‐-―-]?(?:3(?:\.5)?|4(?:o|\.1|\.5|-turbo)?|5(?:\.\d)?|oss)\b",
    "openai":        r"(?i)\bopen\s?-?ai\b",
    "anthropic":     r"(?i)\banthropic\b",
    "copilot":       r"(?i)\bco-?pilot\b",
    "llm":           r"\bLLMs?\b",
    "large-lm":      r"(?i)\blarge[\s-]language[\s-]models?\b",
    "deepseek":      r"(?i)\bdeep\s?seek\b",
    "generative-ai": r"(?i)\bgenerative\s+(?:ai|artificial\s+intelligence|models?\s+such)\b",
    "ai-tool":       r"(?i)\bai[\s-](?:assistant|chatbot|tool|model|language\s+model|"
                     r"system)s?\b|\bai[\s-]assisted\b|\bartificial\s+intelligence\s+"
                     r"(?:tool|assistant|model)s?\b",
    "claude-model":  r"(?i)\bclaude\s*[\s.-]?\s*(?:opus|sonnet|haiku|code|instant|ai|[1-9](?:\.\d)?)\b",
    "gemini-model":  r"(?i)\bgemini\s*[\s.-]?\s*(?:pro|flash|ultra|advanced|[1-9](?:\.\d)?)\b",
    "o-series":      r"(?i)\bo[1345][\s-](?:preview|mini|pro)\b",
    "qwen":          r"(?i)\bqwen\b",
    "language-model": r"(?i)\blanguage\s+models?\b",
    "chatbot":       r"(?i)\bchat\s?-?bots?\b",
    "grammarly":     r"(?i)\bgrammarly\b",
}
WEAK = {
    "gpt-generic": r"(?i)\bgpt\b",
    "claude":  r"(?i)\bclaude\b",
    "gemini":  r"(?i)\bgemini\b",
    "llama":   r"(?i)\bllama\b",
    "mistral": r"(?i)\bmistral\b",
    "grok":    r"(?i)\bgrok\b",
    "gemma":   r"(?i)\bgemma\b",
    "kimi":    r"(?i)\bkimi\b",
    "codex":   r"(?i)\bcodex\b",
    "cursor":  r"(?i)\bcursor\s+(?:ai|ide|editor)\b",
}
# Matched, recorded, but NOT counted as LLM assistance: pre-LLM writing aids.
NOT_LLM = {"grammarly"}

# Cue that an ambiguous word is a tool rather than a person / telescope / wind.
TOOL_CUE = re.compile(
    r"(?i)\b(chatgpt|openai|anthropic|deepmind|llms?|large[\s-]language|"
    r"ai\s+(?:tool|assistant|model)|generative\s+ai|language\s+model|gpt|copilot|"
    r"deepseek|model|chatbot|prompt|\bapi\b|version\s+[0-9])")
PERSON_CUE = re.compile(r"\bClaude\s+[A-ZÉ][a-zà-ÿ'’-]{2,}|\bProf\.?\s+Claude\b|"
                        r"\bDr\.?\s+Claude\b")

# Explicit statements of NON-use.
NEGATION = re.compile(
    r"(?i)\b(no|not|never|neither|without|free\s+of|refrain\w*\s+from|"
    r"did\s+not|do\s+not|does\s+not|have\s+not|has\s+not|was\s+not|were\s+not|"
    r"declare\s+that\s+no)\b[^.]{0,120}\b(ai|llms?|large\s+language|chatgpt|"
    r"generative|gpt|language\s+model)|"
    r"\b(ai|llms?|large\s+language\s+models?|chatgpt|generative\s+ai)\b"
    r"[^.]{0,80}\b(was|were|is|are|has|have)\s+not\s+(?:been\s+)?used")

ANYWHERE = re.compile(
    r"(?i)(chat\s?-?\s?gpt|\bgpt[\s-]?[345]\b|\bopen\s?ai\b|\banthropic\b|"
    r"\bco-?pilot\b|\bLLMs?\b|large[\s-]language[\s-]models?|\bdeep\s?seek\b|"
    r"generative\s+(?:ai|artificial)|\bclaude\s*[\s.-]?\s*(?:opus|sonnet|haiku|[1-9])|"
    r"\bgemini\s*[\s.-]?\s*(?:pro|flash|[1-9])|\bqwen\b)")

ABOUT = re.compile(
    r"(?i)\b(large[\s-]language[\s-]models?|LLMs?|chat\s?-?gpt|gpt-[345]\b|"
    r"transformer[\s-]language|foundation\s+models?|generative\s+pre-?trained|"
    r"language\s+models?|AI\s+agents?|generative\s+ai)\b")

_S = {k: re.compile(v) for k, v in STRONG.items()}
_W = {k: re.compile(v) for k, v in WEAK.items()}


def ack_spans(text: str) -> list[tuple[int, int]]:
    spans = []
    for rx in (ACK_HEAD, ACK_INLINE):
        for m in rx.finditer(text):
            start = m.end()
            e = ACK_END.search(text, start + 20)
            spans.append((start, min(e.start() if e else len(text),
                                     start + ACK_WINDOW)))
    spans.sort()
    out: list[list[int]] = []
    for a, b in spans:
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return [(a, b) for a, b in out]


def in_spans(i: int, spans) -> bool:
    return any(a <= i < b for a, b in spans)


class _Timeout(Exception):
    pass


def _alarm(signum, frame):                                       # noqa: ARG001
    raise _Timeout


def classify_guarded(text: str, seconds: int = 25) -> dict | None:
    """classify(), but give up on a text that takes absurdly long.

    Some pdftotext output contains pathological runs (huge whitespace blocks,
    tables rendered as one enormous line) that make even a well-behaved regex
    crawl.  Rather than let one paper hang the whole corpus, we time it out and
    record it; timed-out papers are reported and excluded, never silently
    counted as "no acknowledgment".
    """
    signal.signal(signal.SIGALRM, _alarm)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        return classify(text)
    except _Timeout:
        return None
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


def classify(text: str) -> dict:
    text = normalise(text)
    spans = ack_spans(text)
    refs = refs_start(text)
    # An acknowledgment heading that appears *after* the bibliography (common in
    # two-column layouts where pdftotext reorders) is still a real ack region.
    ack_after_refs = [(a, b) for a, b in spans if a >= refs]

    cands = []
    MAX_MATCHES = 400          # see module docstring: guards pathological texts
    for bucket, table in (("strong", _S), ("weak", _W)):
        for name, rx in table.items():
            for k, m in enumerate(rx.finditer(text)):
                if k >= MAX_MATCHES:
                    break
                i = m.start()
                ctx = text[max(0, i - CUE_RADIUS): m.end() + CUE_RADIUS]
                inside = in_spans(i, spans)
                # Skip anything sitting in the reference list.
                if i >= refs and not in_spans(i, ack_after_refs):
                    continue
                if not (inside or ACK_CUE.search(ctx)):
                    continue
                if BIBLIO_CUE.search(text[max(0, i - 230): i + 230]) and \
                        not ACK_CUE.search(text[max(0, i - 150): i + 150]):
                    continue     # a reference-list entry
                if name in ("gpt-generic", "gpt-n") and GPT_PHYSICS.search(
                        text[max(0, i - 160): i + 160]):
                    continue     # generalised probabilistic theory, not OpenAI
                if bucket == "weak":
                    if name == "claude" and PERSON_CUE.search(
                            text[max(0, i - 60): i + 60]):
                        continue
                    if not TOOL_CUE.search(ctx):
                        continue
                cands.append({
                    "pat": name, "bucket": bucket, "in_ack_section": inside,
                    "pos": i,
                    "snippet": " ".join(
                        text[max(0, i - 320): m.end() + 420].split()),
                })
                break            # one hit per pattern is enough

    llm = [c for c in cands if c["pat"] not in NOT_LLM]
    verdict = "none"
    if llm:
        verdict = "strong" if any(c["bucket"] == "strong" for c in llm) else "weak"

    negated = any(NEGATION.search(c["snippet"]) for c in llm)
    return {
        "has_ack_section": bool(spans),
        "verdict": verdict,
        "patterns": sorted({c["pat"] for c in llm}),
        "in_ack_section": any(c["in_ack_section"] for c in llm),
        "negation_nearby": negated,
        "grammarly": any(c["pat"] == "grammarly" for c in cands),
        "llm_term_anywhere": bool(ANYWHERE.search(text)),
        "anywhere_ctx": [" ".join(text[max(0, m.start() - 240): m.end() + 300].split())
                         for m in list(ANYWHERE.finditer(text))[:4]],
        "snippets": [c for c in cands][:6],
    }


def main() -> None:
    RES.mkdir(exist_ok=True)
    rows, hits, timeouts = [], [], []
    for f in sorted(LIST.glob("*.json")):
        d = json.loads(f.read_text())
        for r in d["sample"]:
            p = TEXT / f"{r['id']}.txt.gz"
            row = {"id": r["id"], "category": d["category"],
                   "month": f"{d['year']:04d}-{d['month']:02d}",
                   "about_llm": bool(ABOUT.search(r["title"] + " " + r["abstract"])),
                   "title": r["title"]}
            if not p.exists():
                rows.append(row | {"verdict": "MISSING"})
                continue
            with gzip.open(p, "rt", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            c = classify_guarded(text)
            if c is None:
                timeouts.append(r["id"])
                rows.append(row | {"verdict": "TIMEOUT"})
                continue
            row |= {"verdict": c["verdict"], "patterns": "|".join(c["patterns"]),
                    "has_ack_section": c["has_ack_section"],
                    "in_ack_section": c["in_ack_section"],
                    "negation_nearby": c["negation_nearby"],
                    "grammarly": c["grammarly"],
                    "llm_term_anywhere": c["llm_term_anywhere"]}
            rows.append(row)
            # The review set is the UNION of (i) acknowledgment-context
            # candidates and (ii) any paper containing an unambiguous LLM term
            # ANYWHERE.  Every member is adjudicated by hand, because the
            # automated context rule misses disclosures that live outside an
            # acknowledgment -- e.g. "Figure 1 (generated by ChatGPT 4o)".
            if c["verdict"] != "none" or c["grammarly"] or c["llm_term_anywhere"]:
                hits.append(row | {"snippets": c["snippets"],
                                   "anywhere_ctx": c["anywhere_ctx"]})

    keys = ["id", "category", "month", "verdict", "patterns", "about_llm",
            "has_ack_section", "in_ack_section", "negation_nearby", "grammarly",
            "llm_term_anywhere", "title"]
    with (RES / "papers.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    with (RES / "hits.jsonl").open("w") as fh:
        for h in sorted(hits, key=lambda h: (h["month"], h["category"])):
            fh.write(json.dumps(h) + "\n")
    if timeouts:
        print(f"!! {len(timeouts)} papers timed out and are excluded: {timeouts}")
    got = sum(1 for r in rows if r["verdict"] not in ("MISSING", "TIMEOUT"))
    ack = sum(1 for r in rows if r["verdict"] in ("strong", "weak"))
    print(f"{len(rows)} sampled, {got} with text, {ack} candidate LLM "
          f"acknowledgments, {len(hits)} snippets for review -> {RES}")


if __name__ == "__main__":
    main()
