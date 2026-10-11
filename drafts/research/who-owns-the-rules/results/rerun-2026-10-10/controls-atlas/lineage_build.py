"""Phase 4c: build lineage.csv from the row table, verify quotes against stored pages, compute timing, write lineage.md."""
import csv, re, os, sys, datetime
D='results/rerun-2026-10-10/controls-atlas/'
L='corpus/b-raw/controls-atlas/lineage/'
# (domain, date, precision, milestone, stage, status, quote, source, key, url, notes)
R=[]
def r(*a): R.append(a)
U=lambda k: open(L+k+'.txt').readline().strip()
# ---------- APIs
r('apis','1999-06','month','HTTP Basic and Digest authentication standardised (static user-ID and password per realm)',1,'industry standard','The "basic" authentication scheme is based on the model that the client must authenticate itself with a user-ID and a password for each realm.','IETF RFC 2617','api-rfc2617','','Static credential; stands in for the API-key era (no dated primary source for API keys found)')
r('apis','2003-02-18','day','OASIS XACML 1.0: standard policy language with policy decision and enforcement points',5,'industry standard','This specification defines an XML schema for an extensible access-control policy language.','OASIS XACML 1.0 specification','api-xacml','','Quote verified with PDF line numbers stripped')
r('apis','2010-04','month','OAuth 1.0 (RFC 5849): delegated, per-client access without sharing credentials',4,'industry standard','OAuth provides a method for clients to access server resources on behalf of a resource owner','IETF RFC 5849','api-rfc5849','','')
r('apis','2012-04','month','HTTP 429 Too Many Requests: rate limiting codified (RFC 6585)',1,'industry standard','The 429 status code indicates that the user has sent too many requests in a given amount of time ("rate limiting").','IETF RFC 6585','api-rfc6585','','Fixed per-user limit')
r('apis','2012-10','month','OAuth 2.0 (RFC 6749): authorization framework with access tokens',4,'industry standard','The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service','IETF RFC 6749','api-rfc6749','','')
r('apis','2012-10','month','OAuth 2.0 access-token scope: grants limited to a stated scope',3,'industry standard','The authorization and token endpoints allow the client to specify the scope of the access request using the "scope" request parameter.','IETF RFC 6749 section 3.3','api-rfc6749','','Same RFC as the row above, different control')
r('apis','2014-02','month','OpenID Connect Core 1.0 final: identity layer on OAuth 2.0',4,'industry standard','OpenID Connect 1.0 is a simple identity layer on top of the OAuth 2.0 protocol.','OpenID Foundation, OpenID Connect Core 1.0','api-oidc','','Date from the specification reference list ("February 2014"); stored page is errata set 2 (2023)')
r('apis','2015-07-09','day','Amazon API Gateway launch: managed front door with traffic management and access control',1,'product feature','Amazon API Gateway handles all of the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, authorization and access control, monitoring','AWS What\'s New','api-apigw2','','Stage is a judgement: central point, static rules')
r('apis','2015-11-25','day','EU PSD2 Article 97: strong customer authentication required for payment account access (binding on payment providers)',4,'legal requirement','Member States shall ensure that a payment service provider applies strong customer authentication where the payer: (a) accesses its payment account online;','Directive (EU) 2015/2366, EUR-Lex','api-psd2','','Date is the act date; sector-specific legal requirement')
r('apis','2016-08-11','day','API Gateway usage plans: per-key throttling and quotas',3,'product feature','If you started to use API Gateway after the usage plans feature was rolled out on August 11, 2016, you will automatically have usage plans enabled for you in all supported Regions.','AWS API Gateway Developer Guide','api-usageplans','','Date from current AWS documentation; InfoQ (api-usageplans-infoq) is secondary corroboration')
r('apis','2018-03-29','day','Open Policy Agent accepted into the CNCF: general-purpose policy engine',5,'product feature','The Open Policy Agent (OPA) is an open source, general-purpose policy engine that enables unified, context-aware policy enforcement across the entire stack.','CNCF blog','api-opa-cncf','','Acceptance date, not first release')
r('apis','2020-01','month','OAuth 2.0 Token Exchange (RFC 8693): impersonation and delegation tokens',4,'industry standard','security tokens employing impersonation and delegation','IETF RFC 8693','api-rfc8693','','Actor/delegation chains')
r('apis','2023-05-10','day','Cedar open-sourced: fine-grained authorization policy language and engine',5,'product feature','You can use Cedar to express fine-grained permissions as easy-to-understand policies enforced in your applications, and you can decouple access control from your application logic.','AWS What\'s New','api-cedar','','')
r('apis','2023-06-13','day','Amazon Verified Permissions generally available (managed Cedar policy store)',5,'product feature','Verified Permissions uses Cedar, an open-source language for access control, allowing you to define permissions as easy-to-understand policies.','AWS What\'s New','api-avp','','')
# ---------- Cloud
r('cloud','2010-07-06','day','Amazon S3 bucket policies (beta): resource-based conditional rules',1,'product feature','Bucket policies can restrict access based on AWS account as well as request-based attributes, such as HTTP referrer and IP address.','AWS What\'s New','cl-s3pol','','Stage is a judgement (static account/IP/referrer conditions). Earlier (2006) account-key control not sourced')
r('cloud','2010-09-02','day','AWS IAM preview beta: users and per-user permissions inside an account',4,'product feature','IAM enables you to create multiple Users and manage the permissions for each of these Users within your AWS Account.','AWS What\'s New','cl-iambeta','','')
r('cloud','2011-05-03','day','AWS IAM generally available with console support',4,'product feature','You can now add users to your AWS Account, set groups and permissions for these users, and enable users to call AWS Service APIs','AWS What\'s New','cl-iam','','')
r('cloud','2017-02-27','day','AWS Organizations generally available with service control policies',5,'product feature','Using AWS Organizations, you can create Service Control Policies (SCPs) that centrally control AWS service use across multiple AWS accounts.','AWS What\'s New','cl-orgs','','')
r('cloud','2018-07-12','day','IAM permissions boundaries: ceiling on the permissions delegated admins can grant',4,'product feature','Now, you can set a permissions boundary to control the maximum permissions employees can grant to the IAM principals (users and roles) that they create and manage.','AWS What\'s New','cl-pb','','')
r('cloud','2019-06-24','day','AWS Control Tower generally available with preventive and detective guardrails',5,'product feature','they can enable pre-configured guardrails – clearly defined rules for security, operations, and compliance – that prevent deployment of resources that don’t conform to policies','AWS What\'s New','cl-ct','','Policy-as-guardrail across accounts')
r('cloud','2022-12-14','day','EU DORA: binding ICT risk-management framework for financial entities (applies from 2025-01-17)',3,'legal requirement','Financial entities shall have in place an internal governance and control framework that ensures an effective and prudent management of ICT risk','Regulation (EU) 2022/2554, EUR-Lex','cl-dora','','Date is the act date; sector-specific; covers cloud use by financial firms')
# ---------- Network
r('network','1989-03','month','Packet-filtering gateway (screend, DEC WRL report): table-driven packet screening',1,'product feature','One way to restrict access is to prevent certain packets from entering or leaving an organization through its gateways.','Mogul, DEC WRL Research Report 89/4','net-mogul','','Ultrix gateway screen; first sourced packet filter')
r('network','2003-02-20','day','HIPAA Security Rule published (effective 2003-04-21): access control and person authentication for health data systems',4,'legal requirement','Implement technical policies and procedures for electronic information systems that maintain electronic protected health information to allow access only to those persons or software programs that have been granted access rights','45 CFR 164.312, Federal Register 68 FR 8334','net-hipaa','','Sector-specific, not network-specific')
r('network','2007-02','month','NIST SP 800-94: intrusion detection and prevention systems guidance',2,'industry standard','An intrusion prevention system (IPS) is software that has all the capabilities of an intrusion detection system and can also attempt to stop possible incidents.','NIST SP 800-94','net-nist80094','','Codification; commercial IPS predates it (unsourced)')
r('network','2007-06-25','day','Palo Alto Networks PA-4000: application-aware next-generation firewall',3,'product feature','a next-generation firewall that gives organizations unmatched visibility into, and policy control over, applications flowing in and out of their networks','Palo Alto Networks press release','net-pan','','')
r('network','2008-10','month','PCI DSS requirement 6.6 supplement: web application firewalls as a security policy enforcement point',2,'industry standard','A web application firewall (WAF) is a security policy enforcement point positioned between a web application and the client end point.','PCI Security Standards Council','net-pcidss','','Contractual industry standard, not statute')
r('network','2009-09','month','NIST SP 800-41 Rev. 1: guidelines codify stateful inspection beyond packet filtering',3,'industry standard','Stateful inspection improves on the functions of packet filters by tracking the state of connections and blocking packets that deviate from the expected state.','NIST SP 800-41 Rev. 1','net-nist80041','','Codification date; Check Point stateful inspection (c. 1994) not sourced from a primary page')
r('network','2014','year','BeyondCorp (Google): access decided per user and device rather than network perimeter',4,'product feature','Virtually every company today uses firewalls to enforce perimeter security. However, this security model is problematic because, when that perimeter is breached, an attacker has relatively easy access to a company’s privileged intranet.','Ward and Beyer, ;login: 39(6)','net-beyondcorp','','Internal deployment described in paper')
r('network','2020-08','month','NIST SP 800-207 Zero Trust Architecture',5,'industry standard','Zero trust (ZT) provides a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions in information systems and services in the face of a network viewed as compromised.','NIST SP 800-207','net-nist800207','','')
r('network','2021-05-12','day','US Executive Order 14028 directs federal adoption of Zero Trust Architecture',5,'legal requirement','The Federal Government must adopt security best practices; advance toward Zero Trust Architecture','Federal Register, Executive Order 14028','net-eo14028','','Binding on federal agencies only')
r('network','2022-01-26','day','OMB M-22-09 federal zero trust strategy with deadlines to end of FY2024',5,'legal requirement','Federal zero trust architecture (ZTA) strategy, requiring agencies to meet specific cybersecurity standards and objectives by the end of Fiscal Year (FY) 2024','OMB memorandum M-22-09','net-m2209','','Binding on federal agencies only')
# ---------- Industrial
r('industrial','1989-06-14','day','EU Machinery Directive 89/392/EEC: essential requirements incl. emergency stop devices',1,'legal requirement','particular attention must be paid to emergency stop devices liable to be subjected to considerable strain','Council Directive 89/392/EEC, EUR-Lex','ind-md89','','Earlier standards (IEC 60204-1, 1981; EN 418, 1992) not sourced')
r('industrial','1992-02-24','day','OSHA Process Safety Management standard (29 CFR 1910.119) final rule',3,'legal requirement','This section contains requirements for preventing or minimizing the consequences of catastrophic releases of toxic, reactive, flammable, or explosive chemicals.','OSHA 29 CFR 1910.119','ind-psm','','Date from the Federal Register final rule (ind-psmfr)')
r('industrial','1998-12-14','day','IEC 61508-1 first edition: functional safety of programmable safety systems',3,'industry standard','Sets out a generic approach for all safety lifecycle activities for systems comprised of electrical and/or electronic and/or programmable electronic components','Standards Council of Canada catalogue entry for IEC 61508-1:1998','ind-iec61508-1998','','Risk-based safety integrity levels')
r('industrial','2003-01-29','day','IEC 61511-1 first edition: safety instrumented systems for the process industry',3,'industry standard','gives requirements for the specification, design, installation, operation and maintenance of a safety instrumented system','Standards Council of Canada catalogue entry for IEC 61511-1:2003','ind-iec61511-2003','','')
r('industrial','2006-05-17','day','EU Machinery Directive 2006/42/EC recast: emergency stop and control-system requirements',1,'legal requirement','located outside the danger zones, except where necessary for certain control devices such as an emergency stop or a teach pendant','Directive 2006/42/EC, EUR-Lex','ind-md2006','','')
r('industrial','2007','year','ANSI/ISA-99.01.01-2007: first document of the industrial cybersecurity series (later ISA/IEC 62443)',3,'industry standard','ANSI/ISA-99.01.01-2007 “Security for Industrial Automation and Control Systems: Concepts, Terminology and Models”. First document of the series.','INCIBE, IEC 62443: evolution of the ISA 99','ind-62443-incibe','','Secondary (Spanish national CERT); ISA primary page not fetched. IEC 62443 dates not sourced')
r('industrial','2023-06-14','day','EU Machinery Regulation 2023/1230: protection against corruption of connected machinery',3,'legal requirement','The machinery or related product shall be designed and constructed so that the connection to it of another device, via any feature of the connected device itself','Regulation (EU) 2023/1230, EUR-Lex','ind-mr2023','','Date is the act date; applies from 2027-01-20 (not verified here)')
# ---------- Water
r('water','1974','year','US Safe Drinking Water Act: national health-based drinking water standards',1,'legal requirement','The Safe Drinking Water Act (SDWA) was originally passed by Congress in 1974 to protect public health by regulating the nation’s public drinking water supply.','US EPA, Overview of the SDWA','wat-sdwa','','SCADA/telemetry adoption (earlier) has no dated primary source found')
r('water','1999-02-05','day','EPA final operator certification guidelines under SDWA section 1419',4,'legal requirement','These guidelines provide States with the minimum standards for the development, implementation and enforcement of operator certification programs for community and nontransient noncommunity public water systems.','Federal Register notice 99-2692 (federalregister.gov API)','wat-opcert','','Binding through loss of 20 percent of State Revolving Fund grants')
r('water','2002-06-12','day','Bioterrorism Act section 401: vulnerability assessments for community water systems, including computer and automated systems',3,'legal requirement','Each community water system serving a population of greater than 3,300 persons shall conduct an assessment of the vulnerability of its system to a terrorist attack or other intentional acts','Public Law 107-188, congress.gov','wat-bioterror','','')
r('water','2011-06','month','NIST SP 800-82: guide to industrial control systems security, naming water and wastewater',3,'industry standard','ICS are typically used in industries such as electric, water and wastewater, oil and natural gas, transportation','NIST SP 800-82 (June 2011 edition, archived)','wat-nist80082','','')
r('water','2018-10-23','day','America\'s Water Infrastructure Act: risk and resilience assessments incl. electronic and automated systems',3,'legal requirement','Each community water system serving a population of greater than 3,300 persons shall conduct an assessment of the risks to, and resilience of, its system.','Public Law 115-270, congress.gov','wat-awia','','')
r('water','2022-12-14','day','EU NIS2 Directive lists drinking water suppliers and distributors in Annex I',3,'legal requirement','Suppliers and distributors of water intended for human consumption as defined in Article 2, point (1)(a), of Directive (EU) 2020/2184','Directive (EU) 2022/2555, EUR-Lex','wat-nis2','','Date is the act date; transposition due 2024-10-17 (not in stored text)')
r('water','2023-10-11','day','EPA withdraws March 2023 memo requiring cybersecurity review in sanitary surveys (reversal)',3,'legal requirement','the U.S. Environmental Protection Agency (EPA) has chosen to rescind the interpretive memorandum issued on March 3, 2023','US EPA Office of Water memorandum','wat-epamemo','','Reversal: attempted binding interpretation, withdrawn after litigation; excluded from timing')
r('water','2024-05-20','day','EPA enforcement alert on cybersecurity of community drinking water systems',3,'legal requirement','issued an enforcement alert outlining the urgent cybersecurity threats and vulnerabilities to community drinking water systems and the steps these systems need to take to comply with the Safe Drinking Water Act','US EPA news release','wat-enfalert','','Enforcement of existing section 1433 duties')

def norm(s):
    s=s.replace('“','"').replace('”','"').replace('’',"'").replace('‘',"'")
    return re.sub(r'\s+',' ',s).strip()
def page(k):
    t=open(L+k+'.txt',errors='ignore').read().split('\n',2)
    assert t[1]=='FETCHED: 2026-10-11',k
    return t[0], t[2]
rows=[]; bad=0
for i,(dom,date,prec,ms,st,stat,q,src,key,_,notes) in enumerate(R,1):
    url,body=page(key); b=norm(body)
    if key=='api-xacml': b=re.sub(r'(?<= )\d{1,3}(?= )','',b); b=re.sub(r'\s+',' ',b)
    ok = norm(q) in b
    nw=len(q.split())
    if not ok or nw>40: bad+=1; print('QUOTE FAIL',key,ok,nw)
    rows.append(dict(id=i,domain=dom,date=date,date_precision=prec,milestone=ms,stage=st,status=stat,quote=q,quote_verified='yes' if ok else 'NO',quote_words=nw,source=src,url=url,source_path=L+key+'.txt',fetched='2026-10-11',notes=notes))
with open(D+'lineage.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows),'rows; quote failures:',bad)

# ---------- timing
def yr(d):
    p=d.split('-'); y=int(p[0]); m=int(p[1]) if len(p)>1 else 7; dd=int(p[2]) if len(p)>2 else 15
    return y+(datetime.date(y,m,dd).timetuple().tm_yday-1)/365.25
def firsts(dom,pred):
    c=[x for x in rows if x['domain']==dom and pred(x) and not x['notes'].startswith('Reversal')]
    return min(c,key=lambda x:yr(x['date'])) if c else None
out=[]; tab=[]
for dom in ['apis','cloud','network','industrial','water']:
    s1=firsts(dom,lambda x:x['stage']==1)
    n=sum(1 for x in rows if x['domain']==dom)
    line={'domain':dom,'n':n,'first_s1':s1}
    for k in (3,4,5):
        line['ge%d'%k]=firsts(dom,lambda x,k=k:x['stage']>=k)
        line['eq%d'%k]=firsts(dom,lambda x,k=k:x['stage']==k)
    line['legal']=firsts(dom,lambda x:x['status']=='legal requirement')
    tab.append(line)
def dy(a,b): return None if (a is None or b is None) else round(yr(b['date'])-yr(a['date']),1)
def cell(a,b):
    v=dy(a,b); return 'n/a' if v is None else f'{v:+.1f} ({b["date"][:4]})'
md=['# Lineage of control regimes in five domains (Phase 4c)','',
'Collected 2026-10-11. Source: `lineage.csv` (%d milestones, every quote verified verbatim against the stored page, 40 words or fewer). Searches and fetches: `lineage-searchlog.csv`. Pages: `corpus/b-raw/controls-atlas/lineage/`.'%len(rows),'',
'## Years from the first sourced stage-1 control to the first control at each stage','',
'Years are measured from the earliest milestone coded stage 1 in the collected set. "First at stage k or above" treats the scale as ordinal; "exactly" requires the stage to match. Dates mark first availability or publication, not adoption. Negative values mean the later stage appears earlier in the sourced record than the stage-1 baseline, which shows the baseline is censored. Year given in brackets.','',
'| Domain | Milestones | First stage 1 | First at stage 3 or above | First at stage 4 or above | First at stage 5 | First legal requirement |','|---|---|---|---|---|---|---|']
for t in tab:
    s1=t['first_s1']
    md.append(f"| {t['domain']} | {t['n']} | {s1['date'] if s1 else 'none'} | {cell(s1,t['ge3'])} | {cell(s1,t['ge4'])} | {cell(s1,t['ge5'])} | {cell(s1,t['legal'])} |")
md+=['','## Same table, stage must match exactly','','| Domain | Exactly stage 3 | Exactly stage 4 | Exactly stage 5 |','|---|---|---|---|']
for t in tab:
    s1=t['first_s1']; md.append(f"| {t['domain']} | {cell(s1,t['eq3'])} | {cell(s1,t['eq4'])} | {cell(s1,t['eq5'])} |")
md+=['','## First legal requirement, by domain','']
for t in tab:
    l=t['legal']; md.append(f"- {t['domain']}: {l['date']}, {l['milestone']} (stage {l['stage']})")
md+=['','## Reading the numbers','',
'- Stage 2 (classifier) is thin outside network security. Only IPS guidance and web application firewalls were coded stage 2; the stage-2 column is therefore left out of the timing table.',
'- Stage assignments are single-coder judgements by this collector. The design calls for two coders and Opus adjudication; that has not been done. Each non-obvious call is flagged in the `notes` column.',
'- Baselines are censored in cloud, industrial and water. The earliest controls (AWS account keys 2006, IEC 60204-1 1981, EN 418 1992, water SCADA telemetry) had no dated primary page that could be fetched, so the first sourced stage-1 row is later than the true first control.',
'- Legal rows are not all comparable. Some are sector-specific (HIPAA, PSD2, DORA) or bind only federal agencies (EO 14028, M-22-09). The EPA memo reversal is kept in the CSV and excluded from timing.',
'- API stage 5 (XACML 2003) appears before the stage-4 and stage-3 rows for OAuth because standards for policy engines were written long before API products adopted them. Product availability for stage 5 is 2018 (OPA) and 2023 (Cedar, Verified Permissions).','',
'## Gaps','',
'- API keys era: no dated primary source found (RFC 2617 Basic authentication stands in at stage 1).',
'- Apigee launch and AWS Config Rules: pages not retrievable or dated.',
'- Azure Policy: Microsoft GA post not found; documentation page has no date, so it is not in the CSV.',
'- Check Point stateful inspection (1994) and Snort (1998): primary vendor pages blocked or undated; stateful inspection is dated by NIST codification (2009) and the application-firewall/IPS rows by NIST 2007 and PCI 2008.',
'- ISO 13850 (first edition 1996), IEC 60204-1, IEC 62443 IEC publication dates: standards-body pages blocked (403) or showing only current editions.',
'- Water SCADA adoption: only an undated trade history was found; EPA cybersecurity pages for the 2023 memo were found only through the withdrawal memo.',
'- FedRAMP (2011) and other cloud legal requirements beyond DORA: FedRAMP pages returned 404.',
'- Wayback Machine: not used (0 requests).']
open(D+'lineage.md','w').write('\n'.join(md)+'\n')
print('\n'.join(md[6:20]))
