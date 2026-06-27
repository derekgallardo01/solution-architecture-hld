# Usage

How to actually use the HLD + diagram templates on a live engagement.

## Step 1 — Fill the HLD per engagement

Copy `hld-template.md` to `hld-<client>.md` and fill it from the discovery
answers (typically the ones captured via the
[ms-delivery-discovery-kit](https://github.com/derekgallardo01/ms-delivery-discovery-kit)).
Keep each section short and **decision-focused** — every paragraph should
state a choice, not a survey of options.

The worked example,
[examples/hld-greenfield-logistics.md](../examples/hld-greenfield-logistics.md),
shows the level of specificity that actually unblocks a build:

- **Components** table names the connector and the auth scope, not just
  "Asana".
- **Data flow** is numbered and concrete — what gets pulled, what gets
  dropped on the floor (and why), what gets logged.
- **Non-functional** specifies the duration target and the schedule — the
  things you'll be measured against post-go-live.
- **Risks & assumptions** is per-risk with an *actual* mitigation, not
  "monitor closely".

## Step 2 — Drop in a diagram

`diagram-template.md` ships with three reusable Mermaid diagrams (scheduled
sync, RAG agent, multi-entity BI). Pick the closest match, adapt the nodes
to the solution, and paste into the HLD's "Architecture diagram" section.
They render directly on GitHub, in VS Code (Mermaid extension), or at
<https://mermaid.live>.

**Tip:** keep the diagram to one screen. If it needs more, split into a
context diagram + a per-component detail diagram.

## Step 3 — Validate before sharing

```bash
python validate.py examples/hld-greenfield-logistics.md   # check a specific file
python validate.py                                        # check every file under examples/
```

The linter flags angle-bracket placeholders like `<project name>` that
slipped through. Run it on every HLD before sharing — a half-finished doc
reaching a client is the most preventable bad first impression.

The validator deliberately **ignores fenced code blocks** so Mermaid
diagrams (which use `-->` and `<` in node labels) don't trigger false
positives.

## Customizing the kit

### Adding a new diagram

Append a new section under `diagram-template.md`. Three things make a
diagram useful in an HLD:

- **Direction matches the data flow.** `LR` for pipelines, `TD` for
  request/response with branches.
- **Node labels include the *technology*, not just the role.** "Schedule
  trigger (Power Automate)" beats "Schedule trigger".
- **At most one decision diamond per diagram.** If you need more, split.

### Adding a new HLD section

Edit `hld-template.md`. Useful additions per engagement type:

- **§Capacity model** for any sync handling > 10k rows/day or a real-time
  endpoint.
- **§Cost model** for anything on Azure consumption tiers.
- **§Rollback plan** for anything that touches a live production system on
  cutover day.

Run validate on the bare template after — it should still emit placeholders
for any field you expect the user to fill.

### Adding a new worked example

Copy your engagement's HLD into `examples/` under a non-real client name.
Run validate — it should pass clean. Add a line to
`tests/test_validate.py` so the new example is regression-tested.

## What this kit is not

- **Not a low-level design.** Component contracts, schemas, and per-call
  error handling belong in a separate LLD doc owned by the build team.
- **Not a requirements doc.** Requirements live in the discovery + SOW; the
  HLD references those, it doesn't restate them.
- **Not exhaustive.** The three diagram archetypes cover most M365 / Power
  Platform work. For something genuinely novel, draw the diagram first and
  retrofit it into the kit.
