# Conventional enterprise controls: what they look like and what they guarantee (Phase 4b, Addendum 2)

Collected 11 October 2026 from official vendor documentation, no sign-ins. 83 control types in `conventional-sources.csv`, 66 stored pages in `corpus/b-raw/controls-atlas/S/`. Every quote was checked verbatim by script against the stored page (whitespace-normalised). Determinism, position and reach are our coding from the documented mechanism; failure modes are only filled where the page states or directly shows one, otherwise "not documented". `required_by` is "product feature" throughout: none of these pages states a legal or standard requirement for the control itself (AWS only says managed rule groups may help satisfy PCI or HIPAA web application firewall requirements).

Capture notes: Salesforce Help, Oracle Docs and the page-text part of SAP Help are script-rendered, so those pages were read in a browser and their text saved, which includes site navigation text before the article. SAP pages are the Access Control 12.0 SP31 user guide and the EAM configuration guide (PDFs). The Oracle overview is the 26C release page. Salesforce developer-docs pages returned 403 to every non-browser fetch.

## Application access control (13)
Salesforce and Microsoft Entra express access as named bundles (permission sets, app roles) assigned to identities, with field-level security below them and sign-in conditions above them. Salesforce permissions are additive; removing access means removing every grant, so muting exists. Entra Conditional Access adds signal-driven decisions (location, device, risk) enforced after first-factor authentication, plus continuous revocation within minutes. What they guarantee: for a configured rule, the same identity and context always gets the same decision. What they cannot: the rule covers only apps registered in the tenant, and documented gaps are specific (nested groups, unsupported clients, restrictions that do not apply to some Salesforce site types). Entra now lists agent identities as policy targets, but supports only Block for them.

## ERP segregation of duties (13)
SAP Access Control and Oracle Advanced Access Controls define risks as combinations of functions or roles that one person should not hold, then check them at three moments: before assignment (access-request simulation, Oracle provisioning rules), after assignment (risk analysis, incidents, periodic review), and for emergency use (SAP firefighter IDs with reason codes and controller log review). The guarantee is on role combinations, not on actions: a conflict is detected or blocked at assignment, but mitigating controls accept residual risk, and firefighter review happens after the fact. Coverage ends at connected systems (Oracle includes other applications only after setup).

## Robotic process automation (18)
UiPath governs bots as accounts: robot accounts and machine keys, roles scoped to folders, credential stores and encrypted credential assets, queue schemas and retry limits, an audit trail. The documentation says plainly that unattended robots need elevated permissions and credentials, so the control surface stops at Orchestrator: what the robot does inside SAP or Salesforce is governed by the credentials it holds there. Attended robots are bounded by the user's own rights. Power Automate controls act on the building blocks: connector groups that cannot exchange data, blocked connectors, action-level allow lists, tenant isolation, environments. Documented gaps: unblockable core connectors, custom connectors outside action control, an Azure DevOps tenant-isolation bug. Power Platform data policies now also cover MCP connectors.

## API gateways and WAFs (24)
These sit at the boundary of an application and act on each request: IP, geo, rate, size, schema, token, managed rules. Most are deterministic (allow lists, rate counters, schema checks) and the vendors say where they leak: AWS WAF default-allow passes anything no rule blocks, inspects only the first 8 to 64 KB of a body, and geo data is approximate; Azure rate limiting is "never completely accurate"; Cloudflare schema detection does not block by itself. Managed rule sets and bot scores are mixed or probabilistic, and AWS says so for bot control. All three vendors already ship LLM-specific checks at this boundary (Azure LLM token limit and content safety, Cloudflare AI Security for Apps), which are classifier-based.

## Feature flags and release controls (15)
LaunchDarkly and Azure App Configuration put the control inside the code path: the application asks the flag service for a decision on each evaluation, using targeting rules, a hash-based percentage, and a kill switch. Deterministic, testable and instantly reversible without redeploying. Governance is around the flag: approvals, role policies with deny-overrides-allow, per-environment rules, release pipelines, snapshots. The one statistical control is guarded rollout, which pauses on a significant metric regression. LaunchDarkly now applies approvals, targeting and guarded rollouts to "AgentControl configs" as well. Failure behaviour when the flag service is unreachable is not in the pages collected.

## Counts
| domain | control types |
|---|---|
| application access control | 13 |
| ERP segregation of duties | 13 |
| robotic process automation | 18 |
| API gateway and WAF | 24 |
| feature flags and release controls | 15 |

## What this suggests for the comparison with AI agent controls
- Determinism: all domains are mostly deterministic; the probabilistic items (bot score, content safety, prompt-injection detection) are the ones borrowed by AI protection.
- Position: access, SoD, RPA and flag controls sit inside logic that is written and testable. Gateways and WAFs are boundary controls and show the leaks boundary controls have (inspection limits, default-allow, approximate classification).
- Reach: every control is bounded by what the company owns or federates; the RPA case shows the same limit as agents, where a held credential carries the identity into systems the control plane does not govern.
- Rules are written as structured policy (roles, conditions, schemas), not plain-language instructions.
