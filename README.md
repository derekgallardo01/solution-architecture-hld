# Solution architecture — HLD & diagram templates

A high-level design (HLD) document template and a matching architecture-diagram
template (Mermaid) for Microsoft / Power Platform solutions — the "show me your
approach" artifact most serious clients ask for before they commit.

## Why it exists

A clear architecture document does two jobs: it forces the design decisions to be
made explicitly (data flow, security, integration points, failure handling), and it
gives the client confidence that the build is thought through. Producing one quickly
and consistently is a repeatable advantage.

## What's inside

| File | Purpose |
|------|---------|
| `hld-template.md` | A high-level design template: context, requirements, solution overview, components, data flow, security, integrations, risks, and a rollout plan. |
| `diagram-template.md` | Mermaid diagram templates (context, component, and sequence) that render directly on GitHub — no diagramming tool required. |

## How to use it

1. Fill `hld-template.md` per engagement; keep each section short and decision-focused.
2. Drop the relevant diagram from `diagram-template.md` and adapt the nodes to the
   solution. Because they're Mermaid, they render in the document and version cleanly.
3. Share as the approach/architecture deliverable before build starts.
