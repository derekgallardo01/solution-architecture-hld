# High-Level Design — <project name>

**Client:** <name> · **Author:** Derek G. · **Date:** <date> · **Status:** Draft

## 1. Context & goal
<What business outcome this delivers, in 2–3 sentences. Who the users are.>

## 2. Solution overview
<One paragraph: the approach and why. Name the platforms (Power Automate, Copilot
Studio, SharePoint, Azure AI, Fabric/Power BI) and how they fit together.>

See **§Architecture diagram** below.

## 3. Components
| Component | Purpose | Technology |
|-----------|---------|------------|
| <Trigger> | <what starts it> | <Power Automate schedule / webhook> |
| <Source> | <where data comes from> | <Asana API / mailbox / form> |
| <Processing> | <transform / classify / extract> | <flow actions / Azure OpenAI> |
| <Store> | <where results land> | <SharePoint list / Excel table / Dataverse> |
| <Surface> | <how users see it> | <Power BI / Teams / email> |

## 4. Data flow
1. <Trigger fires …>
2. <Pull / receive data …>
3. <Map / transform …>
4. <Write to destination …>
5. <Notify / report …>

## 5. Integrations & connectors
- <Connector / API> — <auth method, license needed>

## 6. Security & privacy
- Identity: <service account / app registration / least privilege>
- Data residency & sensitivity: <region, PII handling>
- AI data handling: <block public model training, tenant-bound data>

## 7. Non-functional
- Schedule/volume: <daily, ~N rows> · Error handling: <retry + run log + alert>
- Maintainability: <documented, no-code where possible, owner can edit>

## 8. Risks & assumptions
| Risk / assumption | Impact | Mitigation |
|-------------------|--------|------------|
| <connector rate limit> | <delays> | <batch + retry> |
| <access not granted by date> | <slips timeline> | <flag in SOW> |

## 9. Milestones
<Link to the SOW milestone table.>
