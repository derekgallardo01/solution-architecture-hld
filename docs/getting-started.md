# Getting started

The HLD + diagram templates are the "show me your approach" artifact
clients ask for after the SOW is signed. Here's how to use them.

## 1. Copy the HLD template

```bash
cp hld-template.md hld-<client>.md
```

Fill from the discovery answers (typically from the
[ms-delivery-discovery-kit](https://github.com/derekgallardo01/ms-delivery-discovery-kit)).
Keep each section **decision-focused** — every paragraph should state a
choice, not a survey of options.

The worked examples ([Greenfield Logistics](../examples/hld-greenfield-logistics.md)
and [Whitford Legal](../examples/hld-whitford-legal.md)) show the level
of specificity that actually unblocks a build:

- Components table names the *connector* and the *auth scope*, not just
  "Asana".
- Data flow is numbered and concrete — what gets pulled, what gets
  dropped on the floor (and why), what gets logged.
- Non-functional specifies the duration target and the schedule.
- Risks & assumptions is per-risk with an *actual* mitigation.

## 2. Drop in a diagram

[`diagram-template.md`](../diagram-template.md) ships with three
reusable Mermaid diagrams:
- Scheduled data sync (Asana / Forms → SharePoint Excel)
- Copilot Studio agent over enterprise docs (RAG)
- Multi-entity BI consolidation (Fabric / Power BI)

Pick the closest match, adapt the nodes to the solution, paste into
your HLD's "Architecture diagram" section. Mermaid renders directly on
GitHub, in VS Code (Mermaid extension), or at <https://mermaid.live>.

## 3. Validate before sharing

```bash
python validate.py hld-<client>.md
```

The linter catches angle-bracket placeholders (`<project name>`,
`<connector>`) that slipped through. Run it on every HLD before sharing
— a half-finished doc reaching a client is the most preventable bad
first impression.

The validator deliberately **ignores fenced code blocks** so Mermaid
arrows (which use `<` / `>` in node labels) don't trigger false
positives.

## 4. Share as the approach deliverable before build starts

The HLD is what stakeholders sign off on between SOW and build. If they
push back on the approach, fix the HLD before any code lands. Easier
than rebuilding.

## What to read next

- [Usage](usage.md) · [Diagrams](diagrams.md) · [FAQ](faq.md)
