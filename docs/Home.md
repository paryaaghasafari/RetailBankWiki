---
title: Northvale Demo Bank — Policy & Compliance Wiki — Home
slug: home
url: Home.md
subdomain: general
owner: Office of the Chief Compliance Officer
version: 8.0
effective_date: 2026-01-01
related_pages:
  - path: KYC-Customer-Onboarding-Policy.md
    relationship: Defines how new customers are identified and risk-rated at account opening
  - path: AML-Anti-Money-Laundering-Procedures.md
    relationship: Ongoing transaction monitoring, SAR filing, and CTR thresholds
  - path: Credit-Risk-Assessment-Guidelines.md
    relationship: Underwriting principles, FICO and DTI thresholds, scoring rubric
  - path: Loan-Approval-Thresholds-and-Limits.md
    relationship: Four-tier approval matrix and product-level caps
  - path: Customer-Complaint-Handling-Policy.md
    relationship: Intake, acknowledgement, resolution, and CFPB escalation timelines
  - path: Sanctions-Screening-Procedures.md
    relationship: OFAC SDN / UN / EU list management and PEP screening
related_attachments:
  - attachments/compliance-handbook-v8.pdf
  - attachments/regulatory-circular-2026-02.pdf
  - attachments/credit-policy-manual.pdf
  - attachments/credit-officer-decision-framework.docx
  - attachments/quarterly-compliance-update-q1-2026.docx
keywords:
  - northvale demo bank
  - policy wiki
  - compliance
  - kyc
  - aml
  - credit
  - loan approval
  - complaints
  - sanctions
  - rag corpus
summary_for_retrieval: >
  Landing page for the Northvale Demo Bank policy and compliance wiki. Indexes all six policy areas
  (KYC, AML, Credit Risk, Loan Approval, Complaints, Sanctions) and the five attachment documents.
  All content is fictional and exists for a GenAI RAG capstone demonstration.
---

# Northvale Demo Bank — Policy & Compliance Wiki

> **Fictional content for demonstration only.** Northvale Demo Bank is a fictional U.S. retail bank with approximately 50 branches and approximately 500,000 customers. Every policy, name, number, and procedure on this wiki is invented for the GenAI RAG capstone demonstration. Do not use any of this content as actual banking guidance.

## Summary

This wiki is the central reference for the policies and procedures that govern retail banking operations at Northvale Demo Bank. It consolidates six policy areas — Know-Your-Customer (KYC) customer onboarding, Anti-Money-Laundering (AML) transaction monitoring, credit risk assessment, loan approval thresholds, customer complaint handling, and sanctions screening — into a single set of pages with consistent terminology, defined terms, and cross-references. The wiki is the **canonical source** for branch staff, credit officers, compliance analysts, customer service representatives, and operations engineers who need to answer day-to-day operational questions about policy, procedure, thresholds, timelines, and escalation paths. Each policy page is self-contained: a reader can answer most general questions about that policy from its page alone, and detailed procedure questions are answered by a specific main-content section or by one of the linked attachment documents (the Compliance Handbook, the Credit Policy Manual, Regulatory Circular 2026-02, the Credit Officer Decision Framework, and the Quarterly Compliance Update). Synonyms in common circulation — customer due diligence / CDD, enhanced due diligence / EDD, suspicious activity report / SAR, currency transaction report / CTR, politically exposed person / PEP, debt-to-income / DTI, loan-to-value / LTV, qualified mortgage / QM — are used consistently throughout the wiki so a reader who uses any of these terms can find the relevant content. The wiki and its attachments are the bank's authoritative published policy as of January 1, 2026.

## Definitions

- **The Bank**: Northvale Demo Bank, the fictional U.S. retail bank that this wiki documents.
- **Customer**: Any natural or legal person with at least one open deposit, loan, or service account at the Bank.
- **Branch Staff**: Branch Managers, Personal Bankers, and Tellers who interact with customers in branches.
- **Compliance Staff**: BSA Officer, L1 / L2 AML Analysts, Sanctions Analysts, and Regional Compliance Officers.
- **Credit Officer**: Any individual with delegated credit-approval authority under the four-tier matrix.
- **CSR**: Customer Service Representative, responsible for first-line complaint intake.
- **Wiki**: This collection of policy and procedure pages; the source corpus for the Bank's RAG assistant.

## Contents

This landing page provides a prose walkthrough of the wiki, followed by a Common Workflows narrative that ties the six policy pages together for practitioners. It then lists the attachment documents, a top-level glossary of synonyms, and a See Also section.

## Navigation by Policy Area

The wiki is organized into four functional groupings that mirror the Bank's operating structure:

- **Onboarding & Identity**: [KYC-Customer-Onboarding-Policy.md](KYC-Customer-Onboarding-Policy.md) for new-account identity verification, due diligence, and risk rating; [Sanctions-Screening-Procedures.md](Sanctions-Screening-Procedures.md) for the OFAC SDN, UN, and EU list-management workflows and PEP screening.
- **Financial Crime**: [AML-Anti-Money-Laundering-Procedures.md](AML-Anti-Money-Laundering-Procedures.md) for transaction monitoring, alert triage, SAR filing, and CTR thresholds.
- **Credit & Lending**: [Credit-Risk-Assessment-Guidelines.md](Credit-Risk-Assessment-Guidelines.md) for underwriting principles and scoring rubrics; [Loan-Approval-Thresholds-and-Limits.md](Loan-Approval-Thresholds-and-Limits.md) for the four-tier approval matrix and product-level dollar caps.
- **Customer Service**: [Customer-Complaint-Handling-Policy.md](Customer-Complaint-Handling-Policy.md) for complaint intake, acknowledgement, resolution, and CFPB escalation timelines.

### Key takeaways

- The wiki has six policy pages plus this Home page, organized into four functional groupings.
- Each policy page is self-contained and uses consistent defined terms across the wiki.
- All attachment documents are linked from at least one policy page.
- The wiki is the canonical source as of January 1, 2026; previous versions are superseded.

### Related Procedures

For ingestion guidance and the ground-truth evaluation question set, see [LOAD-CORPUS.md](https://github.com/paryaaghasafari/RetailBankWiki/blob/main/LOAD-CORPUS.md) and [EVAL-QUESTIONS.md](https://github.com/paryaaghasafari/RetailBankWiki/blob/main/EVAL-QUESTIONS.md) in the source repository. These files are meta documentation for the RAG team and are not themselves part of the policy corpus.

## Common Workflows

The following narrative walks through three workflows that touch multiple policy areas. Each workflow names the policy pages a practitioner would consult and explains how they connect.

**Opening a new account for a high-net-worth individual.** A Personal Banker takes the application and runs the standard Customer Identification Program (CIP) checks documented in the KYC policy. CIP must complete within 30 calendar days of the account opening date. Because the applicant is high-net-worth, the CDD risk rating is likely to be Medium or High, in which case Enhanced Due Diligence (EDD) procedures apply — source-of-funds narrative, ownership tree, and senior compliance sign-off. Simultaneously, the applicant's name passes through real-time sanctions screening (OFAC SDN, UN, EU) and PEP screening per the Sanctions Screening Procedures. If a sanctions or PEP match is generated, a Tier 1 Sanctions Analyst has 4 business hours to clear or escalate the match. Once all gates pass, the account opens and the customer is enrolled in ongoing AML monitoring as described in the AML Procedures page.

**Underwriting an unsecured personal loan.** A Credit Officer receives the application packet via the Loan Origination System. The Officer first applies the Credit Risk Assessment Guidelines to confirm FICO and DTI are within product limits (FICO ≥ 660; DTI ≤ 36% for unsecured personal loans). If the application passes the credit gates, the Officer then applies the Loan Approval Thresholds matrix to route the file to the correct approval tier — Branch Manager up to $25,000, Regional Credit Officer up to $100,000, Credit Committee up to $500,000, or Board Credit Committee above $500,000. If FICO or DTI is outside the gate but compensating factors are present, the application is logged as an exception and approved one tier above the normal authority. The Credit Officer Decision Framework attachment is the desk-level companion procedure.

**Handling a customer complaint that may reveal fraud.** A CSR receives a complaint from a customer about a series of unauthorized transactions. Under the Customer Complaint Handling Policy, the CSR acknowledges the complaint within 5 business days, opens a case, and targets resolution within 30 calendar days. While investigating, the CSR identifies patterns suggestive of money laundering or third-party fraud. Under the AML Procedures (cross-referenced from the Complaints policy), the case is escalated to an L1 AML Analyst within 2 business days of identification. If reasonable suspicion is established, a Suspicious Activity Report (SAR) is filed with FinCEN within 30 calendar days of detection (60 days if no suspect has been identified). The customer-facing complaint resolution and the back-end SAR filing run in parallel and are not disclosed to the customer.

### Key takeaways

- Most real-world tasks touch two or more policy pages — the wiki is designed to be navigated by workflow, not just by topic.
- High-risk customers trigger EDD in KYC, additional monitoring in AML, and tighter screening cadences in Sanctions.
- Loan files always touch both Credit Risk and Loan Approval pages.
- Complaints that reveal financial crime trigger the AML SAR workflow in parallel with the customer-facing resolution.

### Related Procedures

For the detailed step-by-step procedures referenced in each workflow, follow the links to the individual policy pages and their attachments.

## Glossary of Top Synonyms

To support retrieval by either the formal term or the common abbreviation, this wiki uses the following pairs consistently:

- **KYC** = Know-Your-Customer = customer onboarding identity verification.
- **CIP** = Customer Identification Program (the U.S. regulatory term for KYC identity collection).
- **CDD** = Customer Due Diligence (risk-rating at and after onboarding).
- **EDD** = Enhanced Due Diligence (the deeper review applied to high-risk customers).
- **AML** = Anti-Money-Laundering (the financial-crime monitoring program).
- **BSA** = Bank Secrecy Act (the underlying U.S. statute for AML obligations).
- **SAR** = Suspicious Activity Report (filed with FinCEN).
- **CTR** = Currency Transaction Report (filed for cash transactions > $10,000).
- **PEP** = Politically Exposed Person.
- **OFAC** = Office of Foreign Assets Control (issues the SDN sanctions list).
- **SDN** = Specially Designated National (the most prominent OFAC sanctions list).
- **FICO** = the standardized U.S. consumer credit score.
- **DTI** = Debt-to-Income ratio (monthly debt / gross monthly income).
- **LTV** = Loan-to-Value ratio (loan amount / appraised collateral value).
- **QM** = Qualified Mortgage (Ability-to-Repay safe harbor with 43% DTI ceiling).
- **HELOC** = Home Equity Line of Credit.
- **PMI** = Private Mortgage Insurance (required above 80% LTV).
- **CFPB** = Consumer Financial Protection Bureau.

## Attachments

- [attachments/compliance-handbook-v8.pdf](attachments/compliance-handbook-v8.pdf) — Consolidated KYC and AML handbook, effective January 1, 2026.
- [attachments/regulatory-circular-2026-02.pdf](attachments/regulatory-circular-2026-02.pdf) — Sanctions screening threshold update, effective March 1, 2026.
- [attachments/credit-policy-manual.pdf](attachments/credit-policy-manual.pdf) — Credit principles, scoring criteria, tiers, monitoring (10-page manual).
- [attachments/credit-officer-decision-framework.docx](attachments/credit-officer-decision-framework.docx) — Desk-level companion to the Credit Policy Manual.
- [attachments/quarterly-compliance-update-q1-2026.docx](attachments/quarterly-compliance-update-q1-2026.docx) — Q1 2026 compliance status, regulatory updates, and Q2 priorities.

## Cross-References

The KYC page is the natural starting point for any customer-lifecycle question because it covers the very first interaction. The AML and Sanctions pages are the financial-crime continuation of the KYC story — they describe what happens after the account is open. The Credit Risk and Loan Approval pages form a pair for any lending question — one covers underwriting principles, the other covers approval authority. The Complaints page intersects with AML when a complaint reveals suspected fraud or money laundering. Across all six pages, the same 24/12/6-month CDD review cycle, the same 30/60-day SAR window, the same 43% / 36% DTI ceilings, and the same 85% Jaro-Winkler sanctions threshold are used as canonical numbers.

## See also

- [KYC Customer Onboarding Policy](KYC-Customer-Onboarding-Policy.md)
- [AML Anti-Money-Laundering Procedures](AML-Anti-Money-Laundering-Procedures.md)
- [Credit Risk Assessment Guidelines](Credit-Risk-Assessment-Guidelines.md)
- [Loan Approval Thresholds and Limits](Loan-Approval-Thresholds-and-Limits.md)
- [Customer Complaint Handling Policy](Customer-Complaint-Handling-Policy.md)
- [Sanctions Screening Procedures](Sanctions-Screening-Procedures.md)
