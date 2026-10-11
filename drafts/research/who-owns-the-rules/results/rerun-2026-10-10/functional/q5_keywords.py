"""Keyword families for Q5 (duty-statement text, case-insensitive; word-boundary on the left, none on the right
so that stems match: "vulnerabilit" matches vulnerability and vulnerabilities)."""
import re

FAMILIES = {
    "security_review": [
        "security review", "security assessment", "security audit", "security testing", "security risk", "security posture",
        "security architecture", "security requirement", "security control", "security vulnerabilit", "security incident",
        "security standard", "security polic", "threat model", "threat assessment", "penetration test", "pen test",
        "vulnerabilit", "secure code", "secure design", "code review for security", "red team", "incident response",
        "AI security", "AI red team",
        "cybersecurity", "information security", "infosec", "SOC 2", "ISO 27001", "NIST", "data protection impact",
    ],
    "ai_governance": [
        "AI governance", "responsible AI", "AI ethics", "ethical AI", "AI risk", "model risk", "AI polic", "AI safety",
        "AI compliance", "EU AI Act", "trustworthy AI", "model governance", "AI oversight", "human oversight",
        "human-in-the-loop", "human in the loop", "algorithmic bias", "algorithmic fairness", "bias testing",
        "bias mitigation", "model validation", "AI standards", "AI regulation", "AI guideline", "AI usage polic",
        "AI audit", "AI controls",
    ],
    "guardrail_permission": [
        "guardrail", "guard rail", "permission", "access control", "role-based access", "RBAC", "least privilege",
        "entitlement", "approval workflow", "policy enforcement", "allowlist", "allow list", "access management",
        "privileged access", "access authorization", "authorization polic", "authorization model", "authorization framework", "access rights", "access request", "segregation of duties",
        "identity and access", "IAM", "approval limit", "approval authority", "delegation of authority", "usage polic",
    ],
    "service_management": [
        "ITIL", "service management", "incident management", "change control", "change advisory", "change request", "service desk",
        "ServiceNow", "problem management", "service level", "SLA", "service catalog", "ticketing", "CMDB",
        "on-call", "runbook", "service request", "release management",
        "help desk", "helpdesk", "ITSM", "problem ticket",
    ],
}

def _compile(words):
    # leading boundary: word start; words that end in a letter get no trailing boundary (stem match) except short acronyms
    parts = []
    for w in words:
        e = re.escape(w).replace(r"\ ", r"[\s\-]")
        if w.isupper() and len(w) <= 6:
            parts.append(r"(?<![A-Za-z])" + e + r"(?![A-Za-z])")
        else:
            parts.append(r"(?<![A-Za-z])" + e)
    return re.compile("|".join(parts), re.I)

# acronyms are matched case-sensitively through the check in `hits`
FAM_RE = {k: _compile(v) for k, v in FAMILIES.items()}
ACRONYMS = {k: {w for w in v if w.isupper() and len(w) <= 6} for k, v in FAMILIES.items()}

def hits(span):
    out = set()
    for fam, rx in FAM_RE.items():
        for m in rx.finditer(span):
            s = m.group(0)
            if any(s.upper() == a.upper() for a in ACRONYMS[fam]) and s != s.upper() and s.lower() not in {"nist"}:
                # acronym written in lower case (e.g. "sla", "iam", "act") is not counted
                continue
            out.add(fam)
            break
    return out
