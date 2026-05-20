# Ground-Truth Evaluation Questions

> **20 ground-truth Q&A pairs** for testing a RAG pipeline built on the Northvale Demo Bank wiki corpus. Use this file to score retrieval, citation accuracy, and out-of-scope refusal. This file is **not** part of the embedding corpus — exclude it from ingestion.
>
> Distribution: **12 positive single-source · 4 positive cross-page · 4 out-of-scope refusal = 20**.
>
> Each question has:
> - `id` — stable identifier
> - `category` — `positive_single` / `positive_cross_page` / `out_of_scope`
> - `question` — the user query, phrased in natural language
> - `expected_answer_summary` — the factual answer in 1–2 sentences (used for answer-correctness scoring)
> - `expected_citations` — relative paths to source files that the RAG pipeline *must* cite for a correct answer
> - `acceptable_alternatives` — additional relative paths that should also count as correct citations (e.g., the attachment that restates the same fact)
> - `expected_behavior` (out-of-scope only) — what a correct system should do
>
> A pipeline that returns the right answer but cites a wrong file should be scored as a **citation failure**, not as a correct answer.

---

## Positive single-source questions (12)

### Q1 — KYC verification window

```yaml
id: Q1
category: positive_single
question: How long does Northvale Demo Bank have to complete identity verification for a new customer account?
expected_answer_summary: >
  The Bank shall complete the Customer Identification Program (CIP) within 30 calendar days
  of the Account Opening Date. If verification is not complete by day 60, the account is
  restricted and closed.
expected_citations:
  - docs/KYC-Customer-Onboarding-Policy.md
acceptable_alternatives:
  - docs/attachments/compliance-handbook-v8.pdf
```

### Q2 — CTR cash threshold

```yaml
id: Q2
category: positive_single
question: At what cash transaction amount must Northvale file a CTR with FinCEN?
expected_answer_summary: >
  Currency Transaction Reports (CTRs) are filed for cash transactions exceeding $10,000 in a
  single day (or aggregated same-day transactions by the same customer), and filing is due
  within 15 calendar days.
expected_citations:
  - docs/AML-Anti-Money-Laundering-Procedures.md
acceptable_alternatives:
  - docs/attachments/compliance-handbook-v8.pdf
```

### Q3 — Minimum FICO for unsecured personal loan

```yaml
id: Q3
category: positive_single
question: What is the minimum FICO score Northvale Demo Bank requires for an unsecured personal loan?
expected_answer_summary: >
  The minimum FICO score for an unsecured personal loan is 660. A co-signer is required if
  the applicant's FICO is between 660 and 700.
expected_citations:
  - docs/Credit-Risk-Assessment-Guidelines.md
acceptable_alternatives:
  - docs/attachments/credit-policy-manual.pdf
```

### Q4 — Tier 2 Regional Credit Officer approval ceiling

```yaml
id: Q4
category: positive_single
question: What is the maximum unsecured loan amount a Regional Credit Officer can approve at Northvale?
expected_answer_summary: >
  A Regional Credit Officer (Tier 2) may approve unsecured loans up to $100,000. Above that
  amount, the application escalates to the Credit Committee (Tier 3).
expected_citations:
  - docs/Loan-Approval-Thresholds-and-Limits.md
acceptable_alternatives:
  - docs/attachments/credit-policy-manual.pdf
  - docs/attachments/credit-officer-decision-framework.docx
```

### Q5 — Complaint acknowledgement SLA

```yaml
id: Q5
category: positive_single
question: How quickly must Northvale Demo Bank acknowledge a customer complaint?
expected_answer_summary: >
  The Bank shall acknowledge every customer complaint within 5 business days of receipt. The
  acknowledgement includes the case number, named case owner, and expected resolution timeline.
expected_citations:
  - docs/Customer-Complaint-Handling-Policy.md
acceptable_alternatives:
  - docs/attachments/compliance-handbook-v8.pdf
```

### Q6 — Sanctions fuzzy-match threshold

```yaml
id: Q6
category: positive_single
question: What similarity threshold does Northvale's sanctions screening engine use?
expected_answer_summary: >
  The sanctions screening engine uses an 85% Jaro-Winkler similarity threshold (effective
  March 1, 2026), raised from the previous 80% threshold by Regulatory Circular 2026-02.
expected_citations:
  - docs/Sanctions-Screening-Procedures.md
acceptable_alternatives:
  - docs/attachments/regulatory-circular-2026-02.pdf
```

### Q7 — Compliance Handbook effective date

```yaml
id: Q7
category: positive_single
question: When did the Northvale Demo Bank Compliance Handbook v8 take effect?
expected_answer_summary: >
  Compliance Handbook Version 8.0 took effect on January 1, 2026. It superseded Version 7.2
  which had been in effect from July 1, 2024.
expected_citations:
  - docs/attachments/compliance-handbook-v8.pdf
acceptable_alternatives:
  - docs/Home.md
```

### Q8 — Regulatory Circular 2026-02 subject

```yaml
id: Q8
category: positive_single
question: What is the subject of Northvale's Regulatory Circular 2026-02?
expected_answer_summary: >
  Regulatory Circular 2026-02 updates the sanctions screening fuzzy-match threshold from 80%
  to 85% Jaro-Winkler, effective March 1, 2026, and reaffirms the 4-business-hour analyst
  review SLA.
expected_citations:
  - docs/attachments/regulatory-circular-2026-02.pdf
acceptable_alternatives:
  - docs/Sanctions-Screening-Procedures.md
```

### Q9 — Q1 2026 training topic

```yaml
id: Q9
category: positive_single
question: What was the mandatory compliance training topic for Q1 2026 at Northvale?
expected_answer_summary: >
  The Q1 2026 mandatory training topic was Enhanced Due Diligence (EDD). Outstanding training
  completions were due by April 30, 2026. Q2 2026 training focuses on Suspicious Activity
  Reporting (SAR).
expected_citations:
  - docs/attachments/quarterly-compliance-update-q1-2026.docx
acceptable_alternatives: []
```

### Q10 — Credit officer decision SLA

```yaml
id: Q10
category: positive_single
question: How quickly is a Credit Officer required to reach a decision on a complete loan application packet?
expected_answer_summary: >
  Credit Officers must reach a decision within 5 business days of receiving a complete
  application packet. Incomplete packets are returned within 1 business day.
expected_citations:
  - docs/attachments/credit-officer-decision-framework.docx
acceptable_alternatives: []
```

### Q11 — Section in the Credit Policy Manual covering LTV

```yaml
id: Q11
category: positive_single
question: Where in Northvale's Credit Policy Manual are loan-to-value (LTV) ratios documented?
expected_answer_summary: >
  LTV ratios are documented in Section 2 (Scoring Criteria) of the Credit Policy Manual,
  which sets the 80% / 95% (with PMI) ceiling for conventional mortgages, 90% combined for
  HELOCs, and 110% of invoice for prime auto loans.
expected_citations:
  - docs/attachments/credit-policy-manual.pdf
acceptable_alternatives:
  - docs/Credit-Risk-Assessment-Guidelines.md
```

### Q12 — Onboarding flow diagram

```yaml
id: Q12
category: positive_single
question: What does the Northvale customer onboarding flow diagram show?
expected_answer_summary: >
  The diagram shows four sequential gates — Application Received, Identity Verification (CIP),
  Sanctions / PEP Screening, and Customer Due Diligence Risk Rating — followed by a High Risk
  decision diamond that routes the file to Enhanced Due Diligence (EDD) with senior approval
  or to the Standard Approval workflow, both converging into Account Opened and Ongoing
  Monitoring Scheduled.
expected_citations:
  - docs/KYC-Customer-Onboarding-Policy.md
  - docs/attachments/onboarding-flow.png
acceptable_alternatives:
  - docs/attachments/compliance-handbook-v8.pdf
```

---

## Positive cross-page (multi-source) questions (4)

### Q13 — CDD review cadence (cross-page #1)

```yaml
id: Q13
category: positive_cross_page
question: How often does Northvale review a customer's CDD risk rating, by risk level?
expected_answer_summary: >
  CDD periodic reviews occur every 24 months for low-risk customers, every 12 months for
  medium-risk customers, and every 6 months for high-risk customers under EDD. The same
  cadence applies at onboarding (KYC) and ongoing (AML).
expected_citations:
  - docs/KYC-Customer-Onboarding-Policy.md
  - docs/AML-Anti-Money-Laundering-Procedures.md
acceptable_alternatives:
  - docs/attachments/compliance-handbook-v8.pdf
```

### Q14 — PEP screening SLA (cross-page #2)

```yaml
id: Q14
category: positive_cross_page
question: How quickly must a potential PEP match be reviewed by an analyst at Northvale?
expected_answer_summary: >
  Potential PEP matches must be reviewed by a Tier 1 Sanctions Analyst within 4 business
  hours of alert generation. The vendor PEP list refreshes daily. The same SLA applies at
  onboarding (KYC) and on the existing customer base (Sanctions).
expected_citations:
  - docs/KYC-Customer-Onboarding-Policy.md
  - docs/Sanctions-Screening-Procedures.md
acceptable_alternatives:
  - docs/attachments/regulatory-circular-2026-02.pdf
```

### Q15 — SAR filing deadline (cross-page #3)

```yaml
id: Q15
category: positive_cross_page
question: A customer complaint reveals possible fraud — how long does Northvale have to file a SAR?
expected_answer_summary: >
  Suspicious Activity Reports are filed with FinCEN within 30 calendar days of detection,
  extendable to 60 calendar days if no suspect has been identified. The same windows apply
  whether the SAR is sourced from AML monitoring or from a customer complaint.
expected_citations:
  - docs/AML-Anti-Money-Laundering-Procedures.md
  - docs/Customer-Complaint-Handling-Policy.md
acceptable_alternatives:
  - docs/attachments/compliance-handbook-v8.pdf
```

### Q16 — 43% DTI mortgage ceiling (cross-page #4)

```yaml
id: Q16
category: positive_cross_page
question: What is the maximum debt-to-income ratio Northvale allows on a Qualified Mortgage?
expected_answer_summary: >
  The maximum DTI for a Qualified Mortgage (QM) is 43%. This ceiling is documented as both a
  credit-risk factor and a hard approval ceiling, and is consistent across credit-risk and
  loan-approval pages.
expected_citations:
  - docs/Credit-Risk-Assessment-Guidelines.md
  - docs/Loan-Approval-Thresholds-and-Limits.md
acceptable_alternatives:
  - docs/attachments/credit-policy-manual.pdf
```

---

## Out-of-scope refusal questions (4)

These topics are **not** documented anywhere in the corpus. A correct RAG response is a graceful refusal that names the gap rather than fabricating an answer.

### Q17 — Cryptocurrency

```yaml
id: Q17
category: out_of_scope
question: What is Northvale Demo Bank's policy on custody of Bitcoin and other cryptocurrencies?
expected_behavior: >
  The system should respond with a graceful refusal indicating that cryptocurrency or digital
  asset policy is not covered in any of the source documents, and should NOT fabricate a
  policy. Acceptable response includes pointing the user to ask the Bank directly or noting
  that the topic is absent from the available corpus.
expected_citations: []
acceptable_alternatives: []
forbidden_content:
  - Any specific policy statement about cryptocurrency
  - Any made-up custody fee or supported coin list
  - Any fabricated regulatory citation
```

### Q18 — Employee vacation days

```yaml
id: Q18
category: out_of_scope
question: How many vacation days do Northvale Demo Bank employees get per year?
expected_behavior: >
  Graceful refusal — employee benefits / HR policies are not in the available corpus. The
  system should not fabricate vacation-day numbers, accrual rules, or holiday schedules.
expected_citations: []
acceptable_alternatives: []
forbidden_content:
  - Any specific vacation-day count
  - Any HR benefits detail
```

### Q19 — Password policy

```yaml
id: Q19
category: out_of_scope
question: What is Northvale Demo Bank's password policy for employees accessing internal systems?
expected_behavior: >
  Graceful refusal — IT security / infosec procedures are not in the available corpus. The
  system should not fabricate password length, rotation cadence, MFA requirements, or related
  technical controls.
expected_citations: []
acceptable_alternatives: []
forbidden_content:
  - Specific password length, complexity, rotation, or MFA requirement
  - Any infosec procedure detail
```

### Q20 — VPN

```yaml
id: Q20
category: out_of_scope
question: Which VPN does Northvale Demo Bank use for remote work and what are the connection requirements?
expected_behavior: >
  Graceful refusal — remote-access / VPN procedures are not in the available corpus. The
  system should not fabricate vendor names, connection requirements, or split-tunneling
  policies.
expected_citations: []
acceptable_alternatives: []
forbidden_content:
  - Any VPN vendor name
  - Any connection-requirement detail
```

---

## Scoring guidance

A simple per-question score is recommended:

- **Answer correctness** (binary or 0–1): Does the response match `expected_answer_summary` semantically? For `out_of_scope`, did the system refuse?
- **Citation accuracy** (binary or 0–1): Does the response cite *every* file in `expected_citations`? Files in `acceptable_alternatives` may substitute for `expected_citations` entries where the substitution makes semantic sense (e.g., citing the attachment that restates a wiki page).
- **Citation precision** (penalty): For `out_of_scope`, citing *any* source file is a precision failure.

A simple aggregate is the **F1 of correctness and citation accuracy across the 20 questions**, computed separately for positive and out-of-scope cohorts to surface failure modes (e.g., good answers with wrong citations, or fabricated answers for out-of-scope questions).
