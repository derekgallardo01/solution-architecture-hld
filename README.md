# Solution architecture — HLD & diagram templates

[![CI](https://github.com/derekgallardo01/solution-architecture-hld/actions/workflows/ci.yml/badge.svg)](https://github.com/derekgallardo01/solution-architecture-hld/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#)

A high-level design (HLD) document template and a matching architecture-diagram
template (Mermaid) for Microsoft / Power Platform solutions — the "show me
your approach" artifact most serious clients ask for before they commit.
Ships with a fully worked HLD example and a placeholder linter so
half-finished documents don't reach a client.

```bash
python validate.py                                  # check examples/ are fully filled in
python validate.py hld-greenfield-logistics.md      # check your draft before sharing
python -m pytest -q                                 # 3 tests gating the kit
```

## Why it exists

A clear architecture document does two jobs: it forces the design decisions
to be made explicitly (data flow, security, integration points, failure
handling), and it gives the client confidence that the build is thought
through. Producing one quickly and consistently is a repeatable advantage.

## What's inside

| File | Purpose |
|------|---------|
| [hld-template.md](hld-template.md) | A high-level design template: context, requirements, solution overview, components, data flow, security, integrations, risks, and a rollout plan. |
| [diagram-template.md](diagram-template.md) | Mermaid diagrams (scheduled sync · RAG agent · multi-entity BI) that render directly on GitHub — no diagramming tool required. |
| [examples/hld-greenfield-logistics.md](examples/hld-greenfield-logistics.md) | A completed HLD for a fictional logistics SMB (Asana → SharePoint sync), threaded with the discovery + SOW example in the discovery & scoping kit. |
| [validate.py](validate.py) | Placeholder linter — flags unfilled `<…>` markers; skips fenced code so Mermaid arrows don't trigger false positives. |
| [tests/](tests/) | Self-tests: example validates clean; bare template still looks like a template; diagram fences aren't false-flagged. |
| [docs/usage.md](docs/usage.md) | Step-by-step usage + how to customize the kit. |

## How to use it

1. Fill [hld-template.md](hld-template.md) per engagement; keep each section
   short and decision-focused. Save as `hld-<client>.md`.
2. Drop the relevant diagram from [diagram-template.md](diagram-template.md)
   and adapt the nodes to the solution. Because they're Mermaid, they render
   in the document and version cleanly.
3. Run `python validate.py hld-<client>.md` before sharing to catch unfilled
   placeholders.
4. Share as the approach/architecture deliverable before build starts.

[docs/usage.md](docs/usage.md) walks the process end-to-end with the worked
example, and covers how to extend the HLD / diagrams per engagement.
