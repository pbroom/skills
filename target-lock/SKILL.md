---
name: target-lock
description: Turn an annotated screenshot, browser comment, or written example of slop into a lasting slop-lop check. Use when the user asks to remember a mistake so it gets checked and fixed in future reviews.
---

# Target Lock

Read the example and the user's annotation. Identify the element or passage, the task it gets in the way of, and the condition under which it becomes a problem. Inspect the source or reproduce the state when accessible. A screenshot can show layout or copy, while behavior and cause need their own evidence. Use the user's interpretation where given. If two plausible interpretations would lead to different checks, ask which one to capture.

## Save the check

Use the [shared profile format](../slop-lop/references/profiles.md). Default to the project that owns the artifact. Resolve its active checkout from the target. Use the user-wide location when requested. If ownership is unclear, ask where the check belongs.

List existing profiles before writing. When the same failure occurs under the same conditions at the chosen scope, refine that profile under its existing ID. A different surface or failure may need its own profile. Preserve existing exceptions and verification steps that still apply. Write the narrowest check the evidence supports, including when to keep an intentional use. Save a sanitized description. Keep raw screenshots, private links, and customer data out of profiles. Validate the saved file and confirm the normal listing finds it at the intended scope.

## Run it and show proof

Replay the saved check on the original or a representative occurrence using the [slop-lop workflow](../slop-lop/SKILL.md). Record what triggered it. When the user's request includes repairing the artifact, fix the confirmed occurrence in the editable target and replay the same state. For capture or review requests, show the finding and proposed repair. Check a nearby intentional use when one is available.

Use the bundled text locator for a stable literal that helps find candidates. If the defect can be asserted repeatably, reuse the target project's existing test or lint workflow when the requested changes include it. Check that the assertion detects the bad case and passes after the fix. For a visual or contextual judgment, record the state and what to inspect.

Link the saved profile and report what it will check, the observed result, and what was verified after any repair. When the artifact or state can't be replayed, identify what evidence is missing and report the profile as saved with replay pending.
