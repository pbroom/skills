---
name: slop-lop
description: Find and fix AI slop in interfaces, copy, and changed code. Use when asked to de-slop work, remove template filler, or rethink overused or misapplied design patterns.
---

# Slop Lop

Work on the target the user names. With no target, start with the current diff, including uncommitted work, or the artifact already under discussion. Ask for a target if neither exists. Apply justified fixes by default. For capture-only work, a critique, an audit-only request, or a read-only artifact, give specific proposed edits.

## Check saved profiles

Discover [saved profiles](references/profiles.md) for the target's project and the user. Read the full profile when its scope matches the work under review. Check the named surface and state for the failure, and inspect the behavior the profile says to preserve. A text match can help you find a candidate. Confirm the user impact in context before editing.

Report the applicable profile IDs and whether each had a confirmed failure, passed within the inspected scope, or remains unverified. For a repair, show the before and after evidence and check that the intended use still works. Use `$target-lock` when the user asks to save an example for future reviews.

## Decide what earns an edit

Identify who is using the work and what they came to do. Inspect the actual artifact and a representative neighboring example when available. For a UI, see it with realistic content and try the main interaction before judging it. Respect the product's vocabulary, visual identity, accessibility requirements, and explicit design choices.

For each suspect choice, name where it appears, the job it might serve, and what it costs someone here. Familiarity can help people recognize a control. Repetition can make items comparable. Keep the choice when it earns its place. A recognizable style alone is weak evidence of a problem or of who made it.

Use these questions where they fit the artifact:

| Look at | Question to answer | Example repair |
|---|---|---|
| Copy | Could this sentence appear in any product? Does removing it lose a fact, instruction, or part of the author's voice? | Cut a promise to “streamline your workflow.” If “Continue” sends an invitation, label it “Send invitation.” Verify the action first. |
| Hierarchy and layout | What gets attention first? Do repeated cards, badges, or oversized headings make the real task harder to find or compare? | Put renewal dates and amounts on shared axes when people compare plans. Keep a card boundary when it groups an item with its own actions. |
| Visual treatment | What does this color, gradient, icon, shadow, or illustration communicate in context? Is every item asking for emphasis? | Remove a decorative glow that obscures a label. Preserve a gradient that encodes elevation and has a readable legend. |
| Interaction and states | Can the person complete the promised action and recover when it fails? What happens with ordinary messy data? | Replace a generic “You're all set” after a partial import with the actual imported count and the available recovery action. Use data the product has. |
| Implementation | Did the changed code add a pass-through abstraction, a comment that narrates syntax, or a fallback that hides a real failure? | Inline a one-use wrapper that adds no behavior. Trace callers and failure paths before touching validation, logging, or error handling. |

## Fix and verify

Start with the choice that most interferes with the task. Compare removing it, repairing it in place, and using an established product pattern. Choose the smallest change that solves the underlying problem. A page organized around the wrong decision may need regrouping even if its typography is polished. Avoid replacing one template with a signature look of your own.

Verify the edited artifact against the original task. For UI changes, repeat the affected interaction and inspect the relevant viewport or state where the problem showed up. For copy, check factual meaning and read it in its surrounding passage. For code, run the closest behavioral checks. Identify any remaining uncertainty if a preview, source fact, or check is unavailable.

Report the consequential edits, what each improved, and what you verified. In review-only mode, pair each finding with its location and a concrete replacement. An already well-judged target can receive a clean pass.
