#!/usr/bin/env bash
# Raw API call to Anthropic — demonstrates that an LLM interaction
# is just a single HTTP request/response pair.

: "${KEY:?Set KEY to your Anthropic API key}"

curl -s https://api.anthropic.com/v1/messages \
  -H "x-api-key: $KEY" \
  -H "content-type: application/json" \
  -H "anthropic-version: 2023-06-01" \
  -d '{"model":"claude-sonnet-4-6",
       "max_tokens":256,
       "messages":[{"role":"user",
         "content":"What is a quark?"}]}'
