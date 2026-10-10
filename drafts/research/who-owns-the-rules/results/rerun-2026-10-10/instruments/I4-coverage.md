# I4 coverage: rule texts read (revision 2)

Output: `I4-required-functions.csv` (111 provisions, 18 columns). The earlier 103-row file is kept as `I4-required-functions-v1.csv`. This revision applies the fixes in `review/I4-review.md` and the coordinator's follow-up instructions.

## Coding rules

- **`rule_type`**: law, regulation or supervisory rule; supervisory guidance; voluntary standard or framework; lab self-policy; platform or commercial rule. **`binding`**: yes, no or comply-or-explain (PRA SS5/18 only). **`addressee`**: provider/developer, deployer/user firm, investment firm, grid entity, platform seller, lab itself, other. Where a provision binds two parties both are listed.
- **`names_role` (one rule everywhere).** Yes when the text requires a specific designated person, function or body to hold the duty, whether or not it gives a title. This covers RTS 6 "a person designated by the senior management", AI Act Art 26(2) "natural persons" assigned oversight, NERC "System Operators", "compliance function", "risk management function", "traders responsible for the algorithm". No when the duty falls only on "the firm", "the deployer" or "the broker or dealer". `role_title` gives the designation as worded, including for untitled designations (e.g. "person designated by the senior management"); it does not distinguish titled from untitled roles. PRA SS5/18 rows are coded `binding = no` (supervisory expectations, "The PRA expects"), per the Opus re-review.
- **`regulates_changes`**: yes when the provision governs how the system's rules, limits or parameters (or, for lab policies, the policy itself) are changed: approval, review, change management, limit-setting or adjustment, a change log that records the approver. No for documentation kept up to date, reclassification of who is the provider, training, plain recordkeeping, and decisions to deploy a model. Unclear: 1 row (SYSC 27.7, definition not in file).
- **`change_owner`**: the person, function or body the text makes responsible for deciding those changes, named as in the text. "none named" when the text puts the duty only on the firm generally (including firm-versus-customer allocations such as RTS 6 Art 20(2) and SEC 15c3-5(d)). Ownership of a lab policy's changes sits in one row per policy (the change-process row), not in the officer row.
- **Versioned policies** (Anthropic RSP v1.0-v3.4, DeepMind FSF v1.0-v3.1, OpenAI PF v2) are merged to one row per provision. `versions` lists each version with its source id; `change_history` states when the provision appeared, changed or disappeared. `source_id` is the latest version holding the quoted wording.
- NIST table quotes are joined from line fragments (PDF text interleaves table columns); the join marker is a space and the note column says so. All 111 quotes were verified by script against the source text and are 40 words or fewer.

## Read and coded

| source id | text | note |
| --- | --- | --- |
| C217f8b25 | RTS 6 (Reg 2017/589) | Arts 1-29 read; annexes not read |
| C9b1da45a | EU AI Act | Arts 4, 9-17, 25, 26, 27, 43(4), 72, 73, 113 read; other articles and annexes keyword-searched |
| C8b5bc20b | AI Act Omnibus (Reg 2026/1744) | Art 4 replacement, Arts 63, 72, 113 changes read; rest keyword-searched |
| CO-SB26-189-act | Colorado SB26-189 signed act (Ch. 131, approved 14 May 2026) | **new**: fetched with curl from `leg.colorado.gov/laws/session-laws/SB26-189/131/download` (the "Session laws" link on the bill page, C5343d573); saved as `corpus/text/CO-SB26-189-act.txt` with the standard header, PDF in `corpus/raw/CO-SB26-189-signed-act.pdf`. Read 6-1-1701 to 6-1-1706 and section 5; 6-1-1707 and exemptions skimmed. Not yet in `index.csv`/`manifest.csv`. |
| C9e5e0522 | SEC Rule 15c3-5 (LII copy) | **new**: read in full |
| C07e09d04 | FINRA Regulatory Notice 15-09 | **new**: read in full (guidance) |
| C6b47f19f | FINRA Regulatory Notice 16-21 | **new**: read the main body (rule scope, Series 57, supervision); Q&A tail skimmed |
| Cef3dde3f | PRA SS5/18 (PDF) | **new**: sections 2, 3, 5, 6 read; rest keyword-searched. Effective date from web page Ce06358c0 (30 Jun 2018) |
| C84c34c54 | NERC PER-003-2 | **new**: read in full; effective date "see Implementation Plan". PER-003-1 (C89b84182) and -0 (Cc067ee19) failed (HTTP 404) |
| C060d8f5f | FCA SYSC 27.7 | **new**: read; only the table of certification functions names algorithmic trading, the definition (SYSC 27.8.23R) is not in the file |
| Ceb232737 | FCA Algorithmic Trading Compliance in Wholesale Markets (Feb 2018, PDF, full review) | **new**: keyword-searched plus sections 3, 4 and 5 read |
| C3db6f9c1 | FCA multi-firm review of algorithmic trading controls (high-level observations) | **new**: read in full; no publication date in the text file |
| Cb1d56448 | NERC PER-005-2 | R1-R6 read |
| C88fe07c0 / C4c17f4ad | NIST AI RMF 1.0 / GenAI profile | GOVERN, MAP, MANAGE tables and selected actions |
| Ce1250697, Cf8fee27a, Cd3aaca50, C72290590, Cda62cdfa, C61ac2283, C6ec8fdac, Cd06596d1, Cf9d2715e | Anthropic RSP v1.0, v2.0, v2.1, v2.2, v3.0, v3.1, v3.2, v3.3, v3.4 | governance sections read; presence of each provision per version checked by script |
| C3c1aad5c | OpenAI Preparedness Framework v2 | governance, SAG, Appendix B read |
| C25f47316, Cf018b703, Cd899a8f2, Ce9065d39 | DeepMind FSF v1.0, v2.0, v3.0, v3.1 | governance and review passages read |

## Summary only, landing page, unreadable or not retrieved (nothing coded unless stated)

| source id | status |
| --- | --- |
| C5343d573, C1b071d1a | Colorado bill page. C1b071d1a is a duplicate of C5343d573 (same bytes, URL differs by case) and holds no act text. **Colorado is now coded from the signed act**, not the page. |
| C2b7df1f2 | Amazon seller-forum notice; Agent Policy text not in the file (1 row coded from the notice) |
| Cefbe2e8e | FCA 2018 review landing page; the full review is Ceb232737 (coded) |
| C5162f8e9 | Anthropic RSP index page; policy text is in the PDFs |
| Cf7a6b942 | ISO/IEC 42001 purchase page, abstract only |
| C9ae49a11 | DeepMind frontier-safety web page: binary noise, unreadable; excluded |
| C459235e1 | Mastercard agentic commerce guide: `needs-browser`, no text file |
| California SB 53 | **not acquired (leginfo blocks scripts)** |

## Remaining limits

- RTS 6 annexes, AI Act annexes and recitals, and the Colorado exemptions in 6-1-1707 were not coded.
- SEC 15c3-5 is a federal rule on broker-dealers with market access; RTS 6, FINRA and PRA texts address trading firms. NERC addresses grid entities. None binds a firm merely for deploying AI, except the AI Act (providers/deployers) and Colorado (developers/deployers).
- Effective dates are those in the texts; two are computed or external and marked as such (NERC PER-005-2, SS5/18 web page). The Omnibus publication date and the 2025 FCA review date are not in the files.
- A firm-level duty ("the investment firm shall set limits") is coded `change_owner = none named`. Counting those as owners would raise the owner count by 17 rows (all `regulates_changes = yes`).
