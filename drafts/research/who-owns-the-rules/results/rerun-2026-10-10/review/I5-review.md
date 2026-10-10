# I5 review: vendor role definitions and certifications

Reviewer: Opus, 2026-10-10. Scope: `triangulation-design.md` sections 3 (I5), 7 and 10; feature rows N03, N13
and N24; `I5-vendor-roles.csv`, `I5-certifications.csv`, `I5-search-log.csv`; saved texts in
`corpus/b-raw/vendor/`. I opened nothing else.

## Verdict

The quotes are accurate. All 19 non-NF quotes appear verbatim in the saved texts, and I checked 12 rows by
hand for role_type and dates. **The dates are the problem.** No row gives a dated first definition of a
vendor agent role. The `first_capture` values are the first Wayback capture of the URL, not of the quoted
text. In at least two rows the quoted text cannot have existed at that capture. The certification table
dates renames and page updates, not launches. As it stands, I5 cannot say whether vendor definitions came
before or after practitioner descriptions. It cannot code the certification part of N03 or N13. N24 can
be coded only partly, from evidence that is already saved but not yet tabulated.

## CRITICAL fixes

1. **`first_capture` is the URL's first capture, not the first capture of the quote. Re-date each row, or
   rename the column.** For each row with a first_capture value, open the Wayback snapshot at that
   timestamp. Record whether the quoted sentence (or the role name) is present, and record the earliest
   snapshot in which it is (`quote_first_seen`). Proven failures:
   - `ms-cs-security-roles` (Copilot Studio, first_capture 20240226230304). The saved page refers to
     Microsoft Agent 365, which was announced in November 2025, and to "agent makers". The February 2024
     page cannot have carried this quote. As it stands, this row would make Microsoft's "admin governs
     agent capabilities" text about 20 months too early.
   - `goog-agentspace-old` (first_capture 20250814104042). The quote "Grants admin-level access to Gemini
     Enterprise resources" comes from a 2026 fetch. The Gemini Enterprise name dates from October 2025, and
     the release notes (`goog-gem-relnotes`, entry dated April 15, 2026) say the "Gemini Enterprise Admin"
     role name was introduced then and "still map[s] to the Discovery Engine admin and user roles". The
     August 2025 page carried different wording.
   - Every other row with a capture date (`ms-entra-owners`, `ms-a365-overview`, `goog-gemini-iam`,
     `aws-agentcore-*`, `wk-agent-studio`, `zd-manage-access`, `ic-fin-teammates`, `an-custom-roles`,
     `okta-agents`) needs the same check before any date is used in an order comparison.

2. **`published_date` holds page-update dates and announcement dates, not definition dates. Label them by
   type.** Add a `date_type` column with the values {definition_published, product_GA, announcement_PR,
   page_last_updated, rename, capture_lower_bound}. Rows to fix:
   - `ms-entra-whatsnew`, "2026-05-01 (page last updated)". The page is the general-availability notice.
     Its item reads "*Deeper* definitions and clarified differences between owners, sponsors, and
     managers", so a sponsor and owner definition existed before this, in the preview. Record 2026-05-01
     as GA/page_last_updated. The first sponsor definition (expected around the Build 2025 preview) is
     missing. This is the single most important vendor role (`sponsor`, "business accountability ...
     without technical administrative access"). See browser pass B1 and B2.
   - `goog-gemini-iam`, "Last updated 2026-10-08". That is an update date. Replace it with the release-note
     dates already in `goog-gem-relnotes`: 2026-04-15 for the Admin and User role names, and 2026-09-21 for
     the "Agent owners" plus admin transfer-of-ownership entry.
   - `wd-asor-pr`, 2025-02-11. This is a **press-release date** for a product announcement, not a product
     or role date, and the row defines no role (role_type `other`). Mark it announcement_PR and exclude it
     from the "first vendor role definition" comparison.
   - `sn-aict-roles`, "2026-03-12 (Yokohama release page, per summarised fetch)". It is unverified (the
     saved text is a JS loader stub) and internally doubtful (Yokohama is an early-2025 family). Set it to
     NF until the browser pass (B5) captures it.

3. **The certification table dates renames and page updates, and has no first certification.**
   - Salesforce, Agentforce Specialist, 2025-03-03. The source (`sf-ai-specialist-rename`, a third-party
     blog dated 2025-02-18) shows that this is the date the **AI Specialist** exam was renamed. Keep it as
     a *rename* event; it is good N24 evidence. It is not the first certification. The predecessor row
     (AI Specialist) has `launch_date` NF and a `date_source` that points at a 2025-02-28 blog post, which
     says nothing about the predecessor's launch. Fill the AI Specialist launch date (B6, B7). Without it,
     Salesforce's first agent-related certification is undated.
   - UiPath Agentic Automation Associate. The `date_source` cites the academy page's first capture,
     20241210120557. That is a capture of a general certifications page, and the text does not show that
     the agentic exam was listed then. It is a capture date posing as a launch date. Delete it, or verify
     the exam is named in that snapshot. The saved launch page is undated except for "offer ends October
     31, 2025".
   - Microsoft AB-620. 2026-04-21 is the study guide's "Last updated" footer, not the launch or beta date.
     Fill from B9.
   - Intercom "Support agent certification". The saved text is about human support work in Intercom and is
     not about agents. Mark it out of scope (not an agent certification) so that it is not counted.

4. **Certification coverage is too thin to name a "first certification" (N03, N13).** Six rows, none
   with a verified launch date. The search log includes queries for ServiceNow and Zendesk certifications
   that produced no row and no NF row; record the null result. Certifications that were not searched and
   that could move the first date by a year or more:
   - Vendor: AWS Certified AI Practitioner (2024) and AWS Generative AI Developer Professional; Google
     Cloud Generative AI Leader (2025); Microsoft Applied Skills for creating agents in Copilot Studio
     (2024–25, earlier than AB-620); Salesforce AI Associate (2023); ServiceNow Now Assist and AI Agent
     credentials.
   - Non-vendor: IAPP AIGP (2024) and ISACA AAIA (2025). N13 asks about "certification" without
     restricting it to vendors. The orchestrator must decide whether N13's certification date is
     vendor-only (I5) or any certification. Either way, record the decision before coding. A non-vendor
     governance certification from 2024 would come before every vendor date in this table.

5. **Several "role" rows do not define an agent role, and would inflate vendor coverage.** Re-code
   role_type, or add an `agent_specific` yes/no column, and count only the "yes" rows in the "first vendor
   role definition" comparison:
   - `an-roles`, Primary Owner. This is an organisation account role (it "can be a service account"), not
     an agent role. `an-custom-roles` is the same.
   - `ic-fin-teammates`, Full access / View only / No access. These are generic workspace roles. The
     agent-specific permission is in `ic-fin-roles` ("Can view Fin and Automation settings ... Fin AI Agent
     tab"), which is saved but not tabulated. Use it instead.
   - `ms-a365-overview`. The quote describes a feature ("Admins can now view all their agents"), not a role
     definition.
   - `wk-changelog-studio`, "Manager (approver)". The managers are line managers under "your existing
     business processes", not a vendor-defined role. Code it as other, or as a reuse of an existing role.
   - `okta-agents`, role_type `owner` with the quote NF. The saved text has no owner wording; the owner
     wording comes only from a search summary. Set role_type to NF until it is captured.

6. **N24 needs a relabelling table that does not exist yet.** The role CSV has no "previous name, new name,
   date" fields. Evidence that is already saved and supports dated relabelling:
   - **Google.** Discovery Engine roles became `discoveryengine.agentspaceAdmin`, then "Gemini Enterprise
     Admin" (2026-04-15, "still map to the Discovery Engine admin and user roles"). Agentspace became part
     of Gemini Enterprise (release note, 2025-10-09).
   - **Salesforce.** The AI Specialist certification became the Agentforce Specialist (2025-02-18
     announcement, 2025-03-03 effective).
   - **Zendesk.** The existing Support Admin role carries over: "any user with the Admin role for Support
     has the Client admin role for AI agents". This is reuse rather than renaming.
   - **UiPath.** `uipath-orch-default-roles` (saved, not tabulated) shows "Agent Memory" added to the
     existing Orchestrator folder permissions. That is reuse, and it is undated.

   That gives two vendors with dated relabelling from saved text, which is the minimum for N24's "two or
   more vendors" threshold. The product-level relabellings that matter most, and that are not captured,
   are: Power Virtual Agents to Copilot Studio (Microsoft); Einstein Copilot to Agentforce (Salesforce);
   Answer Bot to AI agents (Zendesk); Fin's naming history (Intercom); Vertex AI Search to Agentspace
   (Google). See B10 to B14. Add `relabel.csv`
   (vendor, old_name, new_name, object=product|role|cert, date, date_type, source_id, quote) and fill it
   from saved texts first.

7. **Missing vendors that could change "who defined these roles first".** All of these probably come
   before the 2025–26 rows above:
   - **ServiceNow AI Control Tower** (AI Steward, AI Asset Owner). These are named governance roles; the
     row has only a JS stub. Browser (B5).
   - **Salesforce Agentforce and Einstein Copilot permission sets** ("Manage AI Agents" and its
     predecessors). The page is JS-only. Browser (B8), then Wayback for the dates of the Einstein Copilot
     era.
   - **OpenAI ChatGPT Enterprise and workspace agents.** HTTP 403 to curl. Browser (B15, B16). Wayback
     probably works for help.openai.com.
   - **Microsoft Entra Agent ID preview documents (2025).** The URLs probably moved. Use the Wayback
     prefix search for `learn.microsoft.com/en-us/entra/agent-id/*`; the CDX call timed out in this review,
     so retry it.
   - **Earlier role-defining tools.** AI governance platforms such as IBM watsonx.governance (2023) and
     ML-ops persona tools such as SageMaker Role Manager (2022) may define "AI asset owner" or "model
     owner" roles before any agent product existed. Wayback is fine for these. The orchestrator must decide
     whether they are in I5's frame. If they are excluded, record the exclusion: including them could flip
     the "vendor-led" reading.
   - **Okta for AI Agents owner assignment.** Browser (B17).

## Browser pass (real browser, logged in where noted; save the page text and the visible date)

| # | URL | Capture |
| --- | --- | --- |
| B1 | https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers (click "Previous versions" or open the GitHub history through the "Edit" link) | Earliest commit or ms.date that contains "Sponsors provide business accountability" |
| B2 | https://web.archive.org/web/2025*/learn.microsoft.com/en-us/entra/agent-id/* | Earliest 2025 page that defines a sponsor or owner, with its timestamp and the sentence |
| B3 | https://web.archive.org/web/20240226230304/https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance, then later snapshots | Whether the quote is present; the first snapshot in which it is |
| B4 | https://web.archive.org/web/20250814104042/https://cloud.google.com/agentspace/docs/access-control | The role IDs and description wording as of August 2025 |
| B5 | https://www.servicenow.com/docs/r/_yCRwrQYX6H0b46tCsDNZA/TSKwR8PkgQG9yG2O9fuJEw | The definitions of AI Steward and AI Asset Owner, the release family and the page date |
| B6 | https://admin.salesforce.com/blog/2024/prepare-for-the-salesforce-ai-specialist-exam-and-agentforce | Post date; AI Specialist exam launch date |
| B7 | https://trailheadacademy.salesforce.com/certificate/exam-agentforce-specialist---AI-201 | Exam details. Also check Wayback for the AI Specialist page's first capture, and confirm that the exam is named in that snapshot |
| B8 | https://help.salesforce.com/s/articleView?id=ai.agent_builder_studio.htm&language=en_US | The definition of the "Manage AI Agents" permission and the release named in the page |
| B9 | https://learn.microsoft.com/en-us/credentials/certifications/ (AB-620 exam page) plus the Microsoft Learn blog or Tech Community announcement | AB-620 beta and GA dates; any earlier Applied Skills credential for Copilot Studio agents |
| B10 | Microsoft announcement of Copilot Studio replacing Power Virtual Agents (Ignite 2023 blog) | Rename date and sentence |
| B11 | Salesforce newsroom: Einstein Copilot to Agentforce (2024) | Date and sentence |
| B12 | Google Cloud blog: Agentspace launch, and its relation to Vertex AI Search | Date and sentence |
| B13 | https://support.zendesk.com/hc/en-us/articles/8357756905626-Understanding-user-roles-for-AI-agents-Advanced (needs JS; sign-in may be required) | Role definitions and the article's "Updated" date |
| B14 | Intercom Fin release notes or changelog | Date Fin was called "AI agent", and any Fin-specific certification at academy.fin.ai |
| B15 | https://help.openai.com/en/articles/8266401-managing-members-workspace-roles-and-seats-in-chatgpt-enterprise-and-edu | Role definitions; "Updated" date |
| B16 | https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business | The Owner, Can edit and Can chat definitions; date |
| B17 | https://help.okta.com/oie/en-us/Content/Topics/ai-agents/ai-agents.htm and its child "register agent" pages | The owner-assignment sentence; release date (release notes) |
| B18 | https://start.uipath.com/certifications-registration and https://academy.uipath.com/certifications in Wayback | The first snapshot that names "Agentic Automation Associate" |

## Minor issues

- `I5-search-log.csv`: `results_kept` repeats the same text on every line. Give per-query counts, and give
  each CDX result separately (the success, NF or timeout for each URL).
- `ms-entra-manage-owners`: the Agent ID Administrator row has quote NF although the page was saved. Either
  quote the sentence that names the role, or drop the row.
- `aws-agentcore-iam`: a row with no role and no quote. Drop it.
- `ms-cs-authoring-roles.txt` is a 404 page and is not referenced. Note it in the log.
- `sf-admin-blog`, `sf-exam-guide`, `sf-trailhead-cert`, `sf-agentforce-builder` and `sn-aict-roles` are
  error pages or loader stubs. The log should list them as failed captures, not as sources.
- The AWS AgentCore payments rows (2026-06-30) are very late and specific to payments. They are fine as
  rows, but they should not be presented as AWS's first agent roles.
- Add a `posting_wording_match` field (or a separate step) for I5's second test, whether postings copy
  vendor wording. Nothing in I5 does this yet, and the design's "counts against" depends on it.
- The design (section 10) does not state the limit that vendor documentation is rewritten in place. Add
  it: current documentation pages show today's wording, so every vendor date is a lower bound unless a
  dated snapshot or changelog confirms the wording.
