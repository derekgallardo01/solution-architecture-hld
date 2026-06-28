# Changelog

Notable changes to the Solution architecture (HLD + diagram) templates. Dates
are when the change landed on `main`.

## 2026-06-27 — Second worked HLD (Whitford Legal Copilot rollout)
- `examples/hld-whitford-legal.md` — completed HLD for the fictional law
  firm engagement (Copilot Studio + Azure OpenAI + SharePoint + Teams);
  threads with the discovery + SOW examples in the discovery & scoping kit
- `tests/test_validate.py` extended to cover both worked HLDs

## 2026-06-27 — GitHub Actions CI
- `.github/workflows/ci.yml` running pytest + validate on Python 3.11
- CI status badge added to README

## 2026-06-27 — Build-out: worked example + linter + tests + usage doc
- `examples/hld-greenfield-logistics.md` — fully completed HLD for the
  Asana → SharePoint sync engagement
- `validate.py` placeholder linter; skips fenced code blocks so Mermaid
  arrows don't false-positive
- 3 tests covering example validates clean, bare template flagged, diagram
  fences ignored
- `docs/usage.md` — step-by-step usage including diagram selection and
  per-engagement customization
- README expanded with usage steps, file index, link to docs/usage.md

## 2026-06-27 — Initial public release
- `hld-template.md` — HLD document template (context, components, data
  flow, security, integrations, risks, milestones)
- `diagram-template.md` — three reusable Mermaid diagrams (scheduled sync,
  RAG agent, multi-entity BI)
