# Seeded Numeric & Categorical Facts

> Canonical fact register for the Northvale Demo Bank wiki corpus. Every fact below is asserted with **identical numeric values** across all listed source files. This file is **not** part of the embedding corpus — it exists for eval-set design and consistency checking. See `EVAL-QUESTIONS.md` for the ground-truth Q&A set built on these facts.

Each row gives the fact (with its canonical value), the topic it belongs to, every source file that asserts it, and any notes a downstream eval-author should know.

---

## 1. KYC / Onboarding

| Fact | Value | Source Files |
|---|---|---|
| CIP completion window | 30 calendar days from Account Opening Date | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| Account closure deadline if CIP unverified | 60 calendar days | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| Required CIP data points | Legal name, date of birth, residential address, government-issued ID number | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/attachments/compliance-handbook-v8.pdf` |

## 2. CDD Review Cadence (CROSS-PAGE OVERLAP #1)

| Fact | Value | Source Files |
|---|---|---|
| Low-risk review cadence | Every 24 months | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| Medium-risk review cadence | Every 12 months | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| High-risk (EDD) review cadence | Every 6 months | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| EDD artefacts | Source-of-funds narrative, ownership tree, senior compliance sign-off | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/AML-Anti-Money-Laundering-Procedures.md` |

**Cross-page consistency note**: KYC describes onboarding-time CDD; AML describes ongoing CDD. Both pages cite the identical 24/12/6 cadence.

## 3. PEP Screening (CROSS-PAGE OVERLAP #2)

| Fact | Value | Source Files |
|---|---|---|
| PEP vendor list refresh | Daily | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |
| PEP match analyst review SLA | 4 business hours | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |
| Effect of confirmed PEP | Automatic High CDD risk rating + EDD | `docs/KYC-Customer-Onboarding-Policy.md`, `docs/Sanctions-Screening-Procedures.md` |

**Cross-page consistency note**: KYC documents PEP screening at onboarding; Sanctions documents PEP screening on the customer base. Both pages cite identical daily refresh and identical 4-hour SLA.

## 4. AML / SAR / CTR

| Fact | Value | Source Files |
|---|---|---|
| L1 Analyst triage SLA | 2 business days | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| L2 Investigator case-file SLA | 10 business days | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| Continuing-activity SAR cadence | Every 90 days | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| AML look-back period (default) | 180 days for retail | `docs/AML-Anti-Money-Laundering-Procedures.md` |
| Enhanced monitoring duration (after L2 close without SAR) | 180 days | `docs/AML-Anti-Money-Laundering-Procedures.md` |

## 5. SAR Filing (CROSS-PAGE OVERLAP #3)

| Fact | Value | Source Files |
|---|---|---|
| SAR filing window (suspect identified) | 30 calendar days from detection | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/Customer-Complaint-Handling-Policy.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| SAR filing window (no suspect identified) | 60 calendar days from detection | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/Customer-Complaint-Handling-Policy.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| BSA Officer | Signs off on every SAR before filing | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |

**Cross-page consistency note**: AML documents the SAR workflow procedurally; Complaints documents the cross-over from a customer complaint into the SAR workflow. Both pages cite identical 30/60-day deadlines.

## 6. CTR Filing

| Fact | Value | Source Files |
|---|---|---|
| CTR threshold | Cash transactions > $10,000 (single or same-day aggregated) | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| CTR filing window | 15 calendar days from transaction | `docs/AML-Anti-Money-Laundering-Procedures.md`, `docs/attachments/compliance-handbook-v8.pdf` |

## 7. Sanctions Screening

| Fact | Value | Source Files |
|---|---|---|
| Sanctions lists screened | OFAC SDN, U.N. consolidated, E.U. consolidated | `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |
| Sanctions list refresh | Daily | `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |
| Fuzzy-match threshold | 85% Jaro-Winkler (effective March 1, 2026) | `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |
| Previous fuzzy-match threshold | 80% Jaro-Winkler | `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |
| Sanctions match analyst SLA | 4 business hours | `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |
| OFAC blocked-transaction report window | 10 calendar days | `docs/Sanctions-Screening-Procedures.md`, `docs/attachments/regulatory-circular-2026-02.pdf` |

## 8. Credit Scoring & DTI (CROSS-PAGE OVERLAP #4)

| Fact | Value | Source Files |
|---|---|---|
| Min FICO — unsecured personal | 660 | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Min FICO — residential mortgage (QM) | 620 | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |
| Min FICO — HELOC | 680 | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |
| Min FICO — prime auto | 700 | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |
| Min FICO — subprime auto | 580 | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max DTI — unsecured personal | 36% | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max DTI — QM mortgage | 43% | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max DTI — HELOC | 43% | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max DTI — prime auto | 40% | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max LTV — conventional mortgage no PMI | 80% | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max LTV — conventional mortgage with PMI | 95% | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max LTV — HELOC (combined) | 90% | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |
| Max LTV — prime auto | 110% invoice | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/attachments/credit-policy-manual.pdf` |

**Cross-page consistency note**: Credit Risk defines DTI as a risk factor; Loan Approval cites DTI as a hard ceiling at the tier-routing layer. Both pages cite identical 36% / 43% ceilings.

## 9. Loan Approval Tiers

| Fact | Value | Source Files |
|---|---|---|
| Tier 1 unsecured cap | $25,000 (Branch Manager) | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf`, `docs/attachments/credit-officer-decision-framework.docx` |
| Tier 2 unsecured cap | $100,000 (Regional Credit Officer) | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf`, `docs/attachments/credit-officer-decision-framework.docx` |
| Tier 3 unsecured cap | $500,000 (Credit Committee) | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf`, `docs/attachments/credit-officer-decision-framework.docx` |
| Tier 4 unsecured cap | Above $500,000 (Board Credit Committee) | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf`, `docs/attachments/credit-officer-decision-framework.docx` |
| Secured cap at each tier | 4× the unsecured cap | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Single-borrower max unsecured exposure | $250,000 | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Single-borrower max QM mortgage | $2,000,000 | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Single-borrower max HELOC | $500,000 | `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| 2026 conforming loan limit | $766,550 | `docs/Loan-Approval-Thresholds-and-Limits.md` |
| Annual exception rate ceiling | 5% of all originations | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/Loan-Approval-Thresholds-and-Limits.md`, `docs/attachments/credit-policy-manual.pdf` |
| Compensating factors (3 named) | 12-month reserves; guarantor FICO ≥ 740; LTV < 60% on secured | `docs/Credit-Risk-Assessment-Guidelines.md`, `docs/Loan-Approval-Thresholds-and-Limits.md` |

## 10. Loan Servicing / Delinquency

| Fact | Value | Source Files |
|---|---|---|
| Late payment grace period | 15 calendar days | `docs/attachments/credit-policy-manual.pdf`, `docs/Customer-Complaint-Handling-Policy.md` |
| Late fee | $35 | `docs/attachments/credit-policy-manual.pdf`, `docs/Customer-Complaint-Handling-Policy.md` |
| Past-due (30 days) action | Collections call + payment plan | `docs/attachments/credit-policy-manual.pdf` |
| Workout referral threshold | 60 days delinquent | `docs/attachments/credit-policy-manual.pdf` |
| Non-performing threshold | 90 days delinquent | `docs/attachments/credit-policy-manual.pdf` |

## 11. Complaint Handling

| Fact | Value | Source Files |
|---|---|---|
| Complaint acknowledgement SLA | 5 business days from receipt | `docs/Customer-Complaint-Handling-Policy.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| Complaint resolution target | 30 calendar days from receipt | `docs/Customer-Complaint-Handling-Policy.md`, `docs/attachments/compliance-handbook-v8.pdf` |
| CFPB-tracking escalation trigger | 60 calendar days unresolved | `docs/Customer-Complaint-Handling-Policy.md` |
| CFPB regulatory-complaint acknowledgement deadline | 15 calendar days | `docs/Customer-Complaint-Handling-Policy.md` |
| CSR remedy authority (S1) | Up to $50 per case | `docs/Customer-Complaint-Handling-Policy.md` |
| CSR Lead remedy authority (S2) | Up to $250 per case | `docs/Customer-Complaint-Handling-Policy.md` |
| Branch Manager remedy authority (S3) | Up to $2,500 per case | `docs/Customer-Complaint-Handling-Policy.md` |
| Complaint logged in CMS within | 1 business day of receipt | `docs/Customer-Complaint-Handling-Policy.md` |
| Average resolution time (Q1 2026) | 18 calendar days | `docs/Customer-Complaint-Handling-Policy.md`, `docs/attachments/quarterly-compliance-update-q1-2026.docx` |

## 12. Documents — Effective Dates and Identifiers

| Fact | Value | Source File |
|---|---|---|
| Compliance Handbook version | 8.0 | `docs/attachments/compliance-handbook-v8.pdf` |
| Compliance Handbook effective date | January 1, 2026 | `docs/attachments/compliance-handbook-v8.pdf` |
| Credit Policy Manual effective date | January 1, 2026 | `docs/attachments/credit-policy-manual.pdf` |
| Regulatory Circular number | 2026-02 | `docs/attachments/regulatory-circular-2026-02.pdf` |
| Regulatory Circular subject | Sanctions screening threshold update (80% → 85%) | `docs/attachments/regulatory-circular-2026-02.pdf` |
| Regulatory Circular issued | February 14, 2026 | `docs/attachments/regulatory-circular-2026-02.pdf` |
| Regulatory Circular effective | March 1, 2026 | `docs/attachments/regulatory-circular-2026-02.pdf` |
| Quarterly Compliance Update period | Q1 2026 | `docs/attachments/quarterly-compliance-update-q1-2026.docx` |
| Quarterly Compliance Update Q1 training topic | Enhanced Due Diligence (EDD) | `docs/attachments/quarterly-compliance-update-q1-2026.docx` |
| Quarterly Compliance Update Q2 training topic | Suspicious Activity Reporting (SAR) | `docs/attachments/quarterly-compliance-update-q1-2026.docx` |
| Credit Officer Decision Framework effective | January 1, 2026 | `docs/attachments/credit-officer-decision-framework.docx` |
| Credit Officer decision SLA | 5 business days per complete packet | `docs/attachments/credit-officer-decision-framework.docx` |
| Decision letter to customer SLA | 2 business days from decision | `docs/attachments/credit-officer-decision-framework.docx` |

## 13. The Bank

| Fact | Value | Source Files |
|---|---|---|
| Bank name | Northvale Demo Bank | All wiki pages, all attachments |
| Branch count | Approximately 50 | `docs/Home.md` |
| Customer count | Approximately 500,000 | `docs/Home.md` |
| Status | Fictional — for GenAI RAG capstone demo | All wiki pages, all attachments |

---

## Expected Refusal Topics (deliberately OMITTED from corpus)

These topics are **not** documented anywhere in the wiki or its attachments. A correct RAG implementation should refuse to answer questions about them. Each is the basis for one out-of-scope eval question in `EVAL-QUESTIONS.md`.

| Topic | Test question |
|---|---|
| Cryptocurrency / digital assets policy | Does the Bank custody Bitcoin? |
| Employee benefits / HR | How many vacation days do Bank employees get? |
| IT security / password policy | What's the Bank's password policy for internal systems? |
| Remote-access / VPN procedures | What VPN does the Bank use for remote work? |

These topics were deliberately excluded so the RAG team can validate graceful out-of-scope handling.
