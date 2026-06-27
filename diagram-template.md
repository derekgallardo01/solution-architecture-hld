# Architecture diagram templates (Mermaid)

Edit these per client. Render on GitHub, in VS Code (Mermaid extension), or at
<https://mermaid.live> → export PNG for decks.

## A. Scheduled data-sync automation (e.g. Asana → SharePoint/Excel)

```mermaid
flowchart LR
    T["⏰ Schedule trigger\n(Power Automate)"] --> P["Pull approved entries\n(Asana connector / API)"]
    P --> M["Map fields\nEmployee · Date · Hours · Cost Center"]
    M --> W["Write rows\n(Excel table in SharePoint/OneDrive)"]
    W --> L["Run log + error handling\n(retry, notify on failure)"]
    L --> N["📧 Status notification"]
```

## B. Copilot Studio agent over enterprise docs (RAG)

```mermaid
flowchart TD
    U["👤 User in Teams"] --> A["Copilot Studio agent"]
    A --> R["Retrieve relevant docs\n(SharePoint / Dataverse index)"]
    R --> G["Grounded answer + citations\n(Azure OpenAI / Foundry)"]
    G --> A
    A --> E{"Confident?"}
    E -- "yes" --> U
    E -- "no / sensitive" --> H["Escalate to human\n(assign + notify)"]
```

## C. Multi-entity BI consolidation (Fabric / Power BI)

```mermaid
flowchart LR
    subgraph Sources
      Q1["QuickBooks Co. 1"]; Q2["QuickBooks Co. 2"]; Qn["… Co. N"]
    end
    Q1 --> I["Ingest\n(Fabric pipeline / dataflow)"]
    Q2 --> I
    Qn --> I
    I --> MAP["Map to standardized\nchart of accounts"]
    MAP --> MODEL["Star schema\n+ DAX measures"]
    MODEL --> DASH["Exec dashboard\nMTD/YTD · Budget vs Actual · PY"]
```

> Tip: keep the diagram to one screen. If it needs more, split into a context
> diagram + a per-component detail diagram.
