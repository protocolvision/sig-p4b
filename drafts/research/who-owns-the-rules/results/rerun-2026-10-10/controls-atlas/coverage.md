# Coverage (all coded controls, documented gaps excluded)

2046 controls (65 gap rows excluded), 46 products and protocols.

## By object (products documenting at least one control)

| object                                              |   controls |   products |   groups |
|:----------------------------------------------------|-----------:|-----------:|---------:|
| Logs, traces and audit records                      |        165 |         39 |        8 |
| Identity, credentials and access rights             |        287 |         38 |        7 |
| AI inventory, lifecycle and policy management       |        234 |         33 |        8 |
| Usage, spend and rate limits                        |        130 |         33 |        7 |
| Agent tools and actions                             |        382 |         32 |        8 |
| Harmful and off-limits content                      |        177 |         30 |        7 |
| Sensitive data in prompts and outputs               |         71 |         30 |        8 |
| Data and files the AI can reach                     |        108 |         23 |        7 |
| Stored data: retention, training use and encryption |         92 |         22 |        6 |
| Model choice, routing and caching                   |         74 |         20 |        7 |
| Autonomy and human handover                         |        141 |         19 |        8 |
| Prompt attacks and untrusted input                  |         55 |         19 |        6 |
| Network destinations                                |         79 |         18 |        7 |
| Answer accuracy and presentation                    |         51 |         14 |        6 |

## By mechanism

| mechanism           |   controls |   products |
|:--------------------|-----------:|-----------:|
| Transform or steer  |        486 |         45 |
| Block or switch off |        370 |         42 |
| Allow-list or grant |        525 |         41 |
| Record and report   |        151 |         39 |
| Cap a quantity      |        169 |         35 |
| Detect and flag     |        200 |         34 |
| Require a human     |        145 |         26 |

## By enforcement point

| enforcement_point   |   controls |   products |
|:--------------------|-----------:|-----------:|
| logging_audit       |        196 |         42 |
| identity_permission |        333 |         38 |
| lifecycle           |        236 |         38 |
| input               |        171 |         35 |
| tool_action         |        269 |         34 |
| spend_rate          |        114 |         31 |
| data_access         |        179 |         30 |
| human_approval      |        180 |         27 |
| output              |        172 |         26 |
| model_call          |         96 |         22 |
| network_egress      |        100 |         22 |

## Products per object by group (A business platforms, B cloud runtimes, C model providers, D coding agents, E guardrails, F gateways, G identity/governance, H protocols)

| object                                              |   A |   B |   C |   D |   E |   F |   G |   H |
|:----------------------------------------------------|----:|----:|----:|----:|----:|----:|----:|----:|
| AI inventory, lifecycle and policy management       |   9 |   3 |   3 |   6 |   1 |   2 |   5 |   4 |
| Agent tools and actions                             |   8 |   3 |   2 |   6 |   3 |   4 |   2 |   4 |
| Answer accuracy and presentation                    |   4 |   3 |   0 |   2 |   3 |   1 |   0 |   1 |
| Autonomy and human handover                         |   8 |   1 |   1 |   4 |   1 |   1 |   1 |   2 |
| Data and files the AI can reach                     |   9 |   0 |   2 |   5 |   1 |   2 |   2 |   2 |
| Harmful and off-limits content                      |   7 |   4 |   4 |   3 |   5 |   5 |   2 |   0 |
| Identity, credentials and access rights             |   9 |   4 |   5 |   6 |   0 |   6 |   4 |   4 |
| Logs, traces and audit records                      |   9 |   6 |   4 |   5 |   2 |   5 |   5 |   3 |
| Model choice, routing and caching                   |   5 |   3 |   2 |   3 |   0 |   5 |   1 |   1 |
| Network destinations                                |   2 |   3 |   2 |   5 |   0 |   1 |   3 |   2 |
| Prompt attacks and untrusted input                  |   5 |   3 |   0 |   2 |   5 |   2 |   0 |   2 |
| Sensitive data in prompts and outputs               |   7 |   4 |   1 |   3 |   5 |   4 |   2 |   4 |
| Stored data: retention, training use and encryption |   6 |   4 |   5 |   4 |   0 |   0 |   2 |   1 |
| Usage, spend and rate limits                        |   9 |   5 |   3 |   4 |   2 |   6 |   0 |   4 |
