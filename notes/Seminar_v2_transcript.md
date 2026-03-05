# Transcript: Seminar_v2.m4a

**Duration:** ~21 min 48 s  
**Language:** English  
**Note:** Transcribed with Whisper (tiny model, CPU). Some segments — especially where speech is quieter, faster, or more informal — may be inaccurate.

---

[0.0s – 9.0s] Okay now what we're gonna do is talk through the seminar once again and I will

[9.0s – 17.8s] record my comments as we go along and then we need to fix all the problems that arise.

[17.8s – 24.1s] I'm looking now at the first slide of the presentation. Large language models for this perspective — yep that looks all good.

[24.1s – 29.6s] Now to the next slide. "Why this talk" — good.

[29.6s – 37.2s] And now we have the screenshot of the OpenAI press release — very happy with that.

[37.2s – 43.7s] And now we come to the three moments. Here I have annotated the slide —

[43.7s – 49.8s] the three boxes aren't really equally spaced. So there's kind of a big gap between

[49.8s – 58.0s] November 22 and 2025, and then 2025 and Q4 '25. I realise that chronologically there should be a big gap but it just doesn't look nice, so just

[58.0s – 69.2s] balance the spacing between those two boxes.

[69.2s – 75.1s] And then we come to the "a quick survey" — just get rid of the word "used" on every sentence. I've already scrubbed it out with the annotations.

[75.1s – 84.5s] And put a question mark at the end of those three. So the three points should read: bullet point "ChatGPT, Claude, or Gemini?", bullet point "LLM in IDE to write code?", and bullet point "Coding agent?".

[84.5s – 101.8s] Okay now we move on to the next slide, and here — I don't like how "Q1 '25" sort of breaks at a funny point. Rather the slide should be: "If you tried ChatGPT in Q1 '25, you

[101.8s – 128.9s] probably dismissed LLMs for research. I did." Okay so instead of the comma let's get rid of the comma and put a colon there after 2025.

[128.9s – 139.4s] And we move to the next slide. "I was a skeptic, I'm still annoyed at the models" — that's Q1 '25, yeah that's fine.

[139.4s – 150.5s] And get rid of the quote marks on the slide following that. "LLMs are incredibly capable but maximally untrustworthy" — and not italic, it's sort of inconsistent with the style of the presentation.

[150.5s – 168.4s] Okay now the evidence for why this is done — oh why the "maximally untrustworthy" — there's a five-point list and all the text should be light [...] stealing, buttering, lying — all terrible qualities for research. And there should be a little [inaudible]

[179.4s – 186.6s] Okay. Good mental model of an LLM is "slightly unhinged" instead of "deranged".

[192.5s – 196.5s] [inaudible]

[200.8s – 215.0s] Yeah here we come — not too much punctuation on the slides. Now on to the next slide.

[215.0s – 229.0s] The gap between — [inaudible] — not because a better model is for the technique of domain expertise. This is fine.

[229.0s – 250.0s] Now you want to take another practice of the workload. A subscription to Claude is enough in the queue. Good.

[250.0s – 268.0s] Now we have the slide with the "correct workload" which is deleted. It just looks like — right? This is the one that goes down. So the slide to delete is "put the correct workload..." Okay. The next slide is fine.

[268.0s – 282.0s] "What are the formalisations?" — "Real regretting your site is impossible." Now after this I'm going to ask you to insert a screenshot of the qualifying formalisation which you can see.

[282.0s – 296.0s] Okay. Then after that comes "Accelerating research is possible" — for a truly unique look. The guidance of [inaudible]. And all those can be understood. The human speech is stuck against it.

[296.0s – 330.0s] There we come to "What is in there" — and here we need a new slide after that one. And then comes the new slide. Add slide here to point to the potentials — or you need a paper. So the output of the position is set out. And I'll make you point to the JLM on the page — this slide — and also to PQGVT.jl — my paper. And here I'd want these should be small references at the bottom.

[330.0s – 372.0s] And it should be "Transformers" — should be the title of this slide. And then put a picture of transformers here. So you need on the slide a sketch of the transformers architecture. There are all the areas that are going to go ahead, and I'm going to talk about the changes. Okay.

[372.0s – 383.0s] After this new transformers slide we can jump to "the outside of the union" — that's much better now. On the outside — I don't like — so "from the outside of the union" is fine. "From outside the API boundary" — this is the...

[383.0s – 431.0s] [Several iterations about slide layout] — It's a difficult thing here, I want this to fit on one line, it's breaking. I don't want to wrap it. [...] Again, instead of "from" — we'll delete it. I want this to fit on one line, breaking. [...] Outside the API boundary, this is the result of the behaviour. Sure, the other one's better. So by deleting two words I'm sure you can get the line to fit. [...] I lied to you, but there's last two states — and you see — good, okay.

[439.0s – 470.0s] Next slide is "stateless". Each evaluation is independent, no memory between calls. Not deterministic — well it's temperature. So same input, different output — you sample from a distribution [...] And what "all samples from" — and then just spreading it to it. So I guess you have to get rid of the blue bar.

[470.0s – 541.0s] [Demo section] So this is the general rule. We need to be there to check the rules. [...] Let's control the amount of tokens by [...] And then as I'm doing the demo [...] Okay. The demo worked and then we'll show the [index]. And point out that we're just changing the temperature. Okay, good. So the demo worked.

[553.0s – 617.0s] [Several "okay" pauses]

[591.0s – 617.0s] The next slide says — and how is the output from a distribution over tokens? Instead of "samples one of which we like one after another" — right? So I'll just say we should add "one after another". And I think this "over tokens" should be part of the sentence above. Otherwise it will look like a gap. Okay.

[617.0s – 630.0s] Temperature — the direct connection to the probability distribution. Yeah. We've spoken about temperature. So I'm going to take a [inaudible] — girl state.

[630.0s – 670.0s] And we come to the tokens. For our tokens and the characters and the words, the subword chunks. And our LLM is going to be a function from the language — for this. So the LLM goes one for the first — the reason we're going to have a no-man in the state. And some others, the state is not the same function. It's not this one — although the next token can be in the context of what it seems to be. Good.

[670.0s – 707.0s] Now why doesn't it — like you're having a chat with them? You need to check out here, we're going to be on the phone. So you need to check out — you need to check out an LLM by a single API call. And the box for API is — this is two-part. [...] Not from the slide, but from the one-string [...] we got the C-type version. [...] It's the reality, the one — which is the reality. Now check out [...] turn one — use it. Don't — look, look good.

[711.0s – 727.0s] LLM has the memory in the file and it changes the location. Now we come to the context — put into the looping, and we like it — context window — okay.

[727.0s – 766.0s] So, align the three first statements to the left. Let's just say, as the context grows, it's very close. My condition is great. You can't change the direction, it's really tricky. That is why this is — that is why checking the space [...] It's just a problem — even paying [...] to pull. And then you can see, it's just more. Chat is a memory as a region, it's really fine. Yeah, a function to each.

[768.0s – 800.0s] Okay, so there's two ways in, all right? You can go by the web interface or over the terminal, using the API/SDKs. And this is all great, but the text between the two boxes which says "say, API" underneath is overlapping the boxes. So put "say, API" above the arrows and underneath. Hello, hello, hello — so that it doesn't overlap the two boxes.

[800.0s – 841.0s] Now we come to the agent loop. While not done: response = LLM(system prompt + history + tool calls + results); execute tool call; update history. This is a complete architecture — every coding agent. So the agent: the system prompt + history → LLM takes its input as your prompt, then the agent/client takes the response from the LLM, parses out some tool calls, executes the tool call, sticks it back into the context, and reruns the agent loop.

[841.0s – 923.0s] Okay, what I want to do — I think to slot in here — there's "two ways in" slide — okay, we need a slide after this. [...] This slide about coding agents. I want something like: "Empowering LLMs because autonomous tool use." So we've got this "two ways in" slide, right? This is the two ways in — the way we interface all the time and we're really using the two. But then we need a slide which introduces the whole idea: here the coding agent, which is something that supplies an LLM with autonomous tool use. Just a slide that says that this is another way. So then the slide after that is the agent loop, right — then makes more sense, so it doesn't come out of nowhere. And then what I'm going to do is on that slide which says "Coding Agent, e.g. Claude Code" — that's the thing we're talking about, really, this whole story.

[940.0s – 967.0s] And then after that comes the agent loop — which is good, good. You've got the tools and system. And then we've got: the LLM executes anything, right? It's the scaffold that does. And then — we're going to do a trick — you know, it's incredible — ahaha — we need to set the paper, the web page, we need to sort of refer to that here.

[970.0s – 997.0s] We need to have the — you put the note in the rows — the Thorsten Ball article needs to be referenced here, where the basics of the coding agent are explained.

[1027.0s – 1053.0s] So the Everett has an article [...] that's what everyone's doing it now. So Thorsten Ball — article.

[1053.0s – 1088.0s] This is super weird. So Thorsten Ball has an article: "How to Build a Coding Agent" — it was, oh maybe it's just changed the title. Here we go. So Thorsten Ball has an article. It's called "How to Build an Agent" or "The Emperor Has No Clothes." The article's at ampcode.com. Just like for speaker notes: "How to Build an Agent." Okay, that has to be on a slide which says "Tools."

[1104.0s – 1130.0s] And we come to Claude Code. It calls the code by the same rule: more tools, better prompts. Yeah, that's what we call — you know, lean on what you're doing. But okay, good. Beyond the loop. The real way — [inaudible] — you want to work, you want to check yourself. The basic loop is the simple orchestrator — the basic calling loop. Multi-agent orchestration is good. I like it, some different. Your agent — multi-agent.

[1130.0s – 1150.0s] And then we have to kind of know. So let's get rid of the "live coding" slide — that's the second to last slide. Then we come to "let's try something new" — promises, it's cool, I like that — let's find it.

[1150.0s – 1168.0s] I want to add a slide after the "be sceptical" — now I don't even like the framing title, but you step through — get rid of these steps, get rid of the bar. Just leave the three points, that's okay.

[1168.0s – 1226.0s] But then I want to add a slide. [...] It's a simple picture. It's like a timeline — no, it's not a timeline, it's a line. And then in the middle, there's sort of like a break, or in the middle of the line. And on the left — then the slide is called "Automation." And on the left you have "Labour" and on the right you have "Cognition."

[1226.0s – 1292.0s] And then on the slide — I want to animate, right, you can do it. So what makes "Labour" is: you're calculating — that's a bullet point on the slide. And then: a computer algebra system — passed away. And then it's an "order meeting." So the goal itself is order-meeting: a lot of Labour and a bit of Cognition. And then I want to put a final point. So the AI tools on the right-hand side are going to reach our zone. And this — AI tools is on the side of order-meeting proficient. And so let's — I want a slide about that. So that's a critical slide.

[1292.0s – 1304.0s] And then after that, we've got to — get rid of the line. And currently go, go, go. Let's try to set the gear from us. Let's go. Okay. We'll stop.
