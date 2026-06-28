# Diagrams

This is a templates kit — the diagrams here are about how the HLD fits
into an engagement, not about a runnable system. (The actual
*architecture diagram* archetypes live in
[`diagram-template.md`](../diagram-template.md) — that's what you put
in your client's HLD.)

## 1. Where the HLD sits in the engagement lifecycle

```mermaid
flowchart LR
    SOW["Signed SOW"] --> HLD["HLD<br/>(this kit)"]
    HLD --> CLIENT_REVIEW{"Client reviews<br/>the approach"}
    CLIENT_REVIEW -- "OK" --> BUILD["Build<br/>(per the HLD)"]
    CLIENT_REVIEW -- "concerns" --> ITER["Iterate the HLD<br/>(cheaper than re-building)"]
    ITER --> CLIENT_REVIEW
    BUILD --> ACCEPT["Acceptance<br/>(eval set + UAT)"]
    ACCEPT --> HANDOVER["Handover pack<br/>(includes the HLD as historical record)"]
```

## 2. HLD sections — and which diagram archetype each typically pairs with

```mermaid
flowchart TB
    H1["§1 Context & goal<br/>(prose only)"] --> H2["§2 Solution overview<br/>(1-paragraph + diagram)"]
    H2 --> DIAG_PICK{"Which archetype<br/>fits the solution?"}
    DIAG_PICK -- "Data flowing on a schedule" --> ARC1["A. Scheduled sync"]
    DIAG_PICK -- "User-facing AI agent" --> ARC2["B. RAG / agent"]
    DIAG_PICK -- "Multi-source rollup" --> ARC3["C. BI consolidation"]
    ARC1 --> H3["§3 Components<br/>(table: component / purpose / tech)"]
    ARC2 --> H3
    ARC3 --> H3
    H3 --> H4["§4 Data flow<br/>(numbered steps)"]
    H4 --> H5["§5 Integrations & connectors"]
    H5 --> H6["§6 Security & privacy"]
    H6 --> H7["§7 Non-functional"]
    H7 --> H8["§8 Risks & assumptions<br/>(table: risk / impact / mitigation)"]
    H8 --> H9["§9 Milestones<br/>(link to SOW)"]
```

## 3. The two worked HLDs at a glance

```mermaid
flowchart TB
    subgraph GL["Greenfield Logistics HLD"]
      G1["Pattern: scheduled data sync"]
      G2["Archetype A diagram"]
      G3["6 components<br/>(trigger → pull → map → upsert → log → notify)"]
      G4["4 risks documented"]
    end
    subgraph WL["Whitford Legal HLD"]
      W1["Pattern: RAG / Copilot Studio agent"]
      W2["Archetype B diagram (adapted)"]
      W3["7 components<br/>(Teams → agent → sensitive check → retrieve → generate → cite → analytics)"]
      W4["4 risks documented (incl. classifier misses, AOAI quota)"]
    end
```

The two examples bracket the spectrum: a deterministic data-pipeline
build versus an AI-agent build with sensitive-topic escalation. Most
engagements fit one of these patterns or a small composition of them.

## 4. Validator behaviour — what it does and doesn't catch

```mermaid
flowchart LR
    HLD["hld-X.md"] --> V["python validate.py hld-X.md"]
    V --> SCAN["Scan markdown line-by-line"]
    SCAN --> IN_FENCE{"Inside a ```fenced block?"}
    IN_FENCE -- "yes" --> SKIP["Skip (mermaid arrows aren't placeholders)"]
    IN_FENCE -- "no" --> REGEX{"Matches <[^<>\\n]{1,80}>?"}
    REGEX -- "yes" --> ALLOW{"In ALLOW set?<br/>(br, details, summary, etc.)"}
    REGEX -- "no" --> NEXT["Next line"]
    ALLOW -- "yes (HTML tag)" --> NEXT
    ALLOW -- "no" --> FLAG["Flagged as unfilled placeholder"]
    FLAG --> RPT["Reported with line number"]
    RPT --> EXIT["exit 1 — won't ship"]
```

The validator gates the "I forgot to fill in the client name" class of
mistake. It does NOT validate content correctness — that's what the
client review is for.
