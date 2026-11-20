# Cross-provider profile review

## Choose the reviewer

Use the provider of the runtime that wrote the current draft. For another author, check its run metadata when available. Choose the latest suitable model you can run under the requested provider, honoring any specific model the user asks for.

| Draft author | Reviewer |
|---|---|
| OpenAI, including Codex Sol and Astra | Anthropic Claude Fable or Opus |
| Anthropic, including Claude Fable and Opus | OpenAI Codex Astra or Sol |
| Another provider | A capable model from a different provider |

## Request the review

Use a provider and payload within the user's sharing scope, including any standing approval. Send the sanitized JSON snapshot and the smallest amount of sanitized context needed to judge it. Include its checksum or revision so you can match the reply to the draft. Keep the reviewer read-only and use a fresh session for independent judgment. Use a plain task brief and follow the reviewer's normal permission flow. Ask it to name the actual model, flag actionable gaps, and distinguish a lost safeguard from an optional improvement.

Use Agent Comms when a configured review inbox can deliver to the right provider. Use the approved inbox scope and start the configured runner if needed. Request review of the embedded snapshot so the reviewer can work from the board. For an unversioned profile, use a status post with a `request_reply` and idempotency key to record `state=finished` and `disposition=completed` for the exact request. Confirm the request completed with the review attached. A delivery receipt only establishes pickup.

If the board route is unavailable, use an authenticated provider integration or a one-shot reviewer CLI within the same sharing scope, such as `claude --print` or `codex exec`. Pin the selected model for that invocation, pass the snapshot as text, and use a clean scratch directory with read-only permissions and no unrelated context. Verify the provider and model from runtime metadata or a trusted tool result. If only the reviewer reports its identity, attribute it as such. Use one active reviewer per draft. If no authorized route can deliver the review, report review pending and the actual blocker.

## Apply the feedback

Prioritize findings supported by the user's example or a concrete counterexample. Keep intentional design choices and existing safeguards that still apply. Make the smallest edits that address the findings. If the profile changed during review, compare the current text with the reviewed snapshot and carry forward only feedback that still applies.

Validate and replay the saved revision. Get another pass when the revision materially changes what fires or what gets fixed, or when the user asks. Report the model, the material feedback you applied, and any consequential feedback you held back. Tie the review to the snapshot it covered.
