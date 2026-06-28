# FAQ

## Why HLD before LLD (low-level design)?

The HLD is what the *client* signs off on — components, data flow,
non-functional, risks. The LLD (component contracts, schemas, per-call
error handling) is what *you and the build team* work to. Sharing an
LLD with a client overwhelms them; sharing only the HLD shields them
from internal implementation detail they don't need. Different
audiences, different docs.

## How long should an HLD be?

For a typical Upwork-sized engagement (USD 3k–40k): one page per major
component, total 3–8 pages. Anything longer either has too much LLD
material in it or the engagement is genuinely complex enough to need
splitting.

## Why Mermaid and not draw.io / Lucidchart / Miro?

Mermaid is text — it versions in git, it renders on GitHub, it doesn't
require a separate license, and you can paste it into the HLD next to
the prose that references it. The trade-off: it's less flexible than a
drag-drop tool. For a one-screen architecture diagram that's fine. For
genuinely complex multi-system diagrams, use whatever tool you and the
client both have.

## What does "decision-focused" mean in practice?

"We chose X because Y" is decision-focused. "We could use X, Y, or Z"
is a survey — useful in your head, not in the HLD. The HLD is the
record of which choices you made and why; the survey lives in your
notes or in a separate alternatives-considered appendix if it really
matters.

## How do I document an alternatives-considered section if I need one?

Append an §X Alternatives considered block to the HLD with a table:
"Option A: <choice>, pros: ..., cons: ..., not chosen because: ...".
Three rows max. If the choice was contentious, this section is the
audit trail that protects you when the client asks "why didn't you do
Y" six months in.

## What's the difference between the diagrams in `diagram-template.md` and the new ones in `docs/diagrams.md`?

`diagram-template.md` ships THREE reusable Mermaid diagram archetypes
you adapt per engagement (scheduled sync, RAG agent, BI consolidation).
[`docs/diagrams.md`](diagrams.md) shows how an HLD fits into the
broader engagement flow — meta diagrams about the document itself, not
about a specific solution.

## How do I extend the diagram archetypes?

Add a new section under [`diagram-template.md`](../diagram-template.md).
Three things make a diagram useful in an HLD:
1. **Direction matches data flow** — `LR` for pipelines, `TD` for
   request/response with branches.
2. **Node labels include the technology**, not just the role.
3. **At most one decision diamond per diagram.** If you need more,
   split.

## What if the validator flags a placeholder that's intentional?

Use `{curly braces}` for explanatory substitution markers (e.g. "the
reply uses `{senior associate name}`"). The validator only matches
`<angle brackets>`. The worked Whitford Legal HLD had this exact issue
in its data-flow section — see git history for the fix pattern.
