---
title: Loan Approval Thresholds and Limits
slug: loan-approval-thresholds-and-limits
url: Loan-Approval-Thresholds-and-Limits.md
subdomain: credit
owner: Chief Credit Officer
version: 4.1
effective_date: 2026-01-01
related_pages:
  - path: Credit-Risk-Assessment-Guidelines.md
    relationship: Defines the credit gates (FICO, DTI, LTV) every application must pass before this page's tier routing applies
  - path: KYC-Customer-Onboarding-Policy.md
    relationship: Applicant identity and CDD risk rating feed every approval decision
  - path: Customer-Complaint-Handling-Policy.md
    relationship: Complaints from declined applicants follow the standard intake and resolution flow
related_attachments:
  - attachments/credit-policy-manual.pdf
  - attachments/credit-officer-decision-framework.docx
  - attachments/credit-decision-tree.png
keywords:
  - loan approval
  - approval tiers
  - branch manager
  - regional credit officer
  - credit committee
  - board credit committee
  - dollar limits
  - delegated authority
  - exception escalation
  - dti
  - ltv
summary_for_retrieval: >
  Northvale Demo Bank's loan approval thresholds and limits. Defines four approval tiers — Branch
  Manager (up to $25k unsecured), Regional Credit Officer (up to $100k), Credit Committee (up to
  $500k), Board Credit Committee (above $500k). Secured caps are 4x the unsecured caps. DTI ceilings
  are 36% unsecured and 43% QM mortgage, identical to the Credit Risk Assessment Guidelines.
---

# Loan Approval Thresholds and Limits

> Fictional thresholds for the Northvale Demo Bank GenAI RAG capstone demo. Do not use as real lending guidance.

## Summary

This page defines who in Northvale Demo Bank ("the Bank") has delegated authority to approve a retail loan of a given size. It is the approval-authority companion to the [Credit Risk Assessment Guidelines page](Credit-Risk-Assessment-Guidelines.md), which defines the credit gates (FICO, DTI, LTV) every application must pass before this page's tier-routing applies. The Bank operates a four-tier approval matrix. **Tier 1** authority is held by Branch Managers, who may approve unsecured credit up to $25,000 (secured up to $100,000). **Tier 2** authority is held by Regional Credit Officers, who may approve unsecured credit up to $100,000 (secured up to $400,000). **Tier 3** authority is held by the Credit Committee, which may approve unsecured credit up to $500,000 (secured up to $2,000,000). **Tier 4** authority — the Board Credit Committee — is required for any unsecured exposure above $500,000 or any secured exposure above $2,000,000. The tier required for any given application is the lowest tier whose unsecured cap covers the proposed exposure. Where a single Borrower has multiple facilities at the Bank, aggregate exposure determines the tier. Exceptions to either the credit gates or the tier limits require approval one tier above the normal authority and are documented in the Exception Log reviewed quarterly by the Credit Committee. The Debt-to-Income ceilings cited on this page — 36% unsecured, 43% QM mortgage — are identical to those in the Credit Risk Assessment Guidelines page. Synonyms used throughout: tier / approval tier; cap / ceiling / limit; DTI / debt-to-income; LTV / loan-to-value.

## Definitions

- **Tier**: One of {T1, T2, T3, T4}; the delegated approval level required for a given exposure.
- **Aggregate Exposure**: The sum of all current and proposed credit facilities to the same Borrower (and any guarantors) at the Bank.
- **Unsecured Cap**: The maximum unsecured exposure a tier may approve.
- **Secured Cap**: The maximum secured exposure a tier may approve; equal to 4× the tier's unsecured cap.
- **Branch Manager (T1)**: The manager of a Bank branch; the lowest tier with delegated authority.
- **Regional Credit Officer (T2)**: A credit officer supervising multiple branches; reports to the Chief Credit Officer.
- **Credit Committee (T3)**: A committee chaired by the Chief Credit Officer; meets weekly.
- **Board Credit Committee (T4)**: A subcommittee of the Bank's Board of Directors; meets monthly.
- **Exception**: A deviation from the standard credit gates or tier limits.
- **Related Party**: A Bank officer, director, or immediate family member; cannot be approved by the same tier that holds their relationship.

## Contents

This page covers (1) the four-tier approval matrix with dollar caps, (2) the tier-routing rule and aggregation logic, (3) product-specific dollar limits, (4) the credit decision tree showing how amount maps to tier, (5) exception escalation, (6) DTI thresholds at-a-glance (cross-referenced with the Credit Risk Assessment page), (7) common scenarios, and (8) frequently asked questions.

## 1. Four-Tier Approval Matrix

The Bank's approval authority is delegated in four tiers. The table below restates the matrix that appears in the Credit Policy Manual (Section 3) and the Credit Officer Decision Framework (Section 2). For any application, the required tier is the lowest tier whose unsecured cap covers the proposed exposure. Where a Borrower has multiple facilities at the Bank, aggregate exposure across all facilities determines the tier, not the individual facility size.

| Tier | Authority | Unsecured Cap | Secured Cap | Quorum |
|---|---|---|---|---|
| T1 | Branch Manager | $25,000 | $100,000 | Single approver |
| T2 | Regional Credit Officer | $100,000 | $400,000 | Single approver |
| T3 | Credit Committee | $500,000 | $2,000,000 | Three of five members |
| T4 | Board Credit Committee | Above $500,000 | Above $2,000,000 | Three of five members |

In summary, T1 handles small-ticket unsecured loans (most personal loans, credit-builder loans, and some auto loans), T2 handles mid-sized loans (most jumbo personal loans and most mortgages), T3 handles large secured exposures (jumbo mortgages, commercial-purpose HELOCs), and T4 is reserved for the largest exposures requiring Board-level oversight. The secured caps are exactly 4× the unsecured caps at every tier. The same matrix is reused in the [Credit Officer Decision Framework](attachments/credit-officer-decision-framework.docx) and on the [Credit Risk Assessment Guidelines page](Credit-Risk-Assessment-Guidelines.md).

### Key takeaways

- T1 unsecured cap is $25,000; T2 is $100,000; T3 is $500,000; T4 is anything above.
- Secured caps are 4× unsecured at every tier.
- T3 and T4 require a quorum of three of five committee members.
- The same matrix appears in the Credit Policy Manual and the Credit Officer Decision Framework.

### Related Procedures

The credit gates an application must pass before this matrix applies are documented in [Credit-Risk-Assessment-Guidelines.md](Credit-Risk-Assessment-Guidelines.md), Section 2. The Credit Officer Decision Framework attachment is the desk-level companion procedure.

## 2. Tier Routing and Aggregation

For any single new application, the required tier is the lowest tier whose unsecured cap is greater than or equal to the proposed exposure (or whose secured cap, for secured products, is greater than or equal). When a Borrower has existing facilities at the Bank, the credit officer must aggregate exposure across all facilities — including any joint or guarantor obligations — and use the aggregate to determine the tier. An existing customer with $80,000 in unsecured exposure who applies for an additional $30,000 personal loan must be routed to T2 (because aggregate exposure of $110,000 exceeds the T1 cap), not T1.

Aggregation also applies across products: a customer with a $200,000 mortgage and a $50,000 personal loan has $250,000 aggregate exposure for the purpose of tier routing, even though the mortgage is secured and the personal loan is unsecured. The tier is computed using the secured-cap scale if the aggregate is dominated by secured exposure, and the unsecured-cap scale otherwise; the credit officer documents the choice in the credit memorandum.

### Key takeaways

- Tier is determined by the lowest tier whose cap covers the proposed exposure.
- Aggregate exposure across all facilities — including joint and guarantor — drives the tier.
- Aggregation crosses product types.
- The credit memorandum documents the aggregation choice.

### Related Procedures

The aggregation rule is restated in Section 3 of the [Credit Policy Manual](attachments/credit-policy-manual.pdf).

## 3. Product-Specific Dollar Limits

The following product-specific dollar limits apply alongside the tier matrix. They are the maximum exposure the Bank will originate to a single Borrower for the given product, regardless of approval tier. The table summarises the limits.

| Product | Max Single-Borrower Exposure | Notes |
|---|---|---|
| Unsecured personal loan | $250,000 | Above $250k must be secured |
| Residential mortgage (QM) | $2,000,000 | Jumbo above $766,550 (2026 conforming) |
| HELOC | $500,000 | 90% combined LTV ceiling |
| Prime auto loan | $150,000 | 110% invoice LTV, 72-month max |
| Subprime auto loan | $50,000 | Senior approval required |

The takeaway is that the unsecured single-Borrower exposure ceiling is $250,000 across the Bank — any larger unsecured exposure is declined or must be re-structured as a secured facility. Residential mortgages can reach $2 million on the QM track, with jumbo treatment beginning at the 2026 conforming-loan limit of $766,550. HELOC, prime auto, and subprime auto have their own product-level ceilings.

### Key takeaways

- Unsecured exposure to a single Borrower is capped at $250,000.
- QM mortgage exposure is capped at $2,000,000 per Borrower.
- HELOC ceiling is $500,000.
- Subprime auto loans are capped at $50,000 and require senior approval.

### Related Procedures

These product-level ceilings are restated in Section 2 of the [Credit Policy Manual](attachments/credit-policy-manual.pdf). DTI and LTV product-level ceilings are in [Credit-Risk-Assessment-Guidelines.md](Credit-Risk-Assessment-Guidelines.md), Section 2.

## 4. Credit Decision Tree

The diagram below shows how the credit gate and the amount-based tier routing fit together. Step 1 is the FICO-and-DTI gate, defined in the Credit Risk Assessment page. Step 2 — the focus of this page — is the amount-based tier routing.

![Credit decision tree](attachments/credit-decision-tree.png)

### Figure description

The credit decision tree diagram shows a top blue box "Loan Application" feeding into an amber diamond "FICO >= 660 and DTI <= 36%?". The "No" branch leads to a red "Decline or Refer to Secured Product" box. The "Yes" branch leads into a sequence of amount-based diamonds: "Amount <= $25,000?" routes to a teal "Tier 1 Branch Manager" box; "Amount <= $100,000?" routes to "Tier 2 Regional Credit Officer"; "Amount <= $500,000?" routes to "Tier 3 Credit Committee"; and the final "No" branch routes to a navy "Tier 4 Board Credit Committee" box for any amount above $500,000. The same diagram is reused on the Credit Risk Assessment page because the two pages share the same decision logic.

### Key takeaways

- The tree has two steps: credit gate (Step 1) and tier routing (Step 2).
- Failed Step 1 is decline or referral, not just a higher tier.
- Step 2 is the focus of this page.
- The same diagram is embedded on the Credit Risk Assessment page and in the Credit Policy Manual.

### Related Procedures

The Step 1 logic is detailed in [Credit-Risk-Assessment-Guidelines.md](Credit-Risk-Assessment-Guidelines.md), Section 3. The diagram also appears in Section 4 of the [Credit Policy Manual](attachments/credit-policy-manual.pdf).

## 5. Exception Escalation

An exception is any deviation from the credit gates (Section 2 of the Credit Risk Assessment page) or the tier caps defined here. Exceptions are approved one tier above the tier that would normally hold authority. A T1 application that exceeds the credit gate requires T2 approval; a T2 application that exceeds the tier cap requires T3 approval; a T3 application that exceeds the tier cap requires T4 approval. Every exception is documented in the Exception Log and reviewed quarterly by the Credit Committee.

The Bank's annual exception rate ceiling is 5% of all originations. When the Bank's rolling four-quarter exception rate approaches the ceiling, the Chief Credit Officer convenes a portfolio review and may impose temporary restrictions on exception approvals across one or more tiers. Permissible compensating factors are the same three named in the Credit Risk Assessment page: 12 months of liquid reserves; a guarantor with FICO 740 or higher; LTV below 60% on a secured product.

### Key takeaways

- Exceptions are approved one tier above normal.
- The annual exception rate ceiling is 5% of all originations.
- The Credit Committee reviews the Exception Log quarterly.
- Three named compensating factors: 12-month reserves, FICO 740 guarantor, LTV below 60%.

### Related Procedures

Exception logging is detailed in Section 4 of the [Credit Officer Decision Framework](attachments/credit-officer-decision-framework.docx).

## 6. DTI Thresholds At-a-Glance

This section restates — for reader convenience — the DTI ceilings introduced in the Credit Risk Assessment page. The values are identical by design: the unsecured 36% and the QM-mortgage 43% are the canonical DTI ceilings used throughout the Bank's documentation. An RAG assistant should be able to return either page when asked about DTI; both pages are mutually consistent.

| Product | DTI Ceiling | Tier Required at or Below Ceiling |
|---|---|---|
| Unsecured personal loan | 36% | T1 to T4 depending on amount |
| Residential mortgage (QM) | 43% | T1 to T4 depending on amount |
| HELOC | 43% | T1 to T4 depending on amount |
| Prime auto loan | 40% | T1 to T2 (capped at $150k) |
| Subprime auto loan | 45% | T2 or higher (senior approval) |

In summary, the 36% (unsecured) and 43% (QM mortgage and HELOC) DTI ceilings are the most-cited capacity ceilings on the Bank's books. Applications above the ceiling are approved only as exceptions per Section 5 and only one tier above the tier that would normally have authority. These figures are stable across this page, the Credit Risk Assessment page, and the Credit Policy Manual.

### Key takeaways

- Unsecured DTI ceiling is 36%; QM mortgage and HELOC ceiling is 43%.
- DTI above ceiling requires an exception and one-tier-up approval.
- DTI ceilings are identical here and in the Credit Risk Assessment page.

### Related Procedures

The detailed DTI calculation methodology and the underlying capacity principles are in [Credit-Risk-Assessment-Guidelines.md](Credit-Risk-Assessment-Guidelines.md), Section 5.

## Common Scenarios

**Scenario A — Small unsecured at T1.** A customer applies for a $20,000 unsecured personal loan with FICO 740 and DTI 24%. The application passes the credit gate and routes to T1. The Branch Manager approves. No exception logged.

**Scenario B — Mid-size unsecured at T2.** A customer applies for a $75,000 unsecured personal loan with FICO 720 and DTI 32%. The application passes the gate and routes to T2 (Regional Credit Officer). Approval granted; the credit memorandum cites the existing $20,000 unsecured exposure to the same Borrower, making aggregate exposure $95,000.

**Scenario C — Aggregate exposure pushes up a tier.** A customer with an existing $80,000 unsecured personal loan applies for an additional $30,000 unsecured loan. Aggregate exposure becomes $110,000, exceeding the T1 cap of $25,000 and the T2 cap of $100,000 on the unsecured scale. The application routes to T3 (Credit Committee). The credit memorandum documents the aggregation.

**Scenario D — Mortgage above conforming.** A customer applies for a $1,500,000 jumbo QM mortgage. FICO 780, DTI 38%, LTV 65%. The application passes the gate and routes to T3 because $1.5M exceeds the T2 secured cap of $400,000. The Credit Committee approves. The Borrower is well below the $2 million product ceiling and the 43% DTI ceiling.

**Scenario E — Exception at T1 escalates to T2.** A customer applies for a $20,000 unsecured loan with FICO 720 and DTI 38% (above the 36% unsecured ceiling). The Branch Manager identifies 14 months of liquid reserves as a compensating factor, logs an exception, and routes the file to T2. The Regional Credit Officer approves on the strength of the reserves. The exception is queued for the next quarterly Credit Committee review.

### Key takeaways

- Most loans are approved at T1 or T2.
- Aggregate exposure across all the Borrower's facilities determines the tier.
- Exceptions require one-tier-up approval.
- Jumbo mortgages routinely route to T3.

### Related Procedures

For complaint handling when a customer disputes a tier-related decline, see [Customer-Complaint-Handling-Policy.md](Customer-Complaint-Handling-Policy.md).

## FAQ

**Q1. What's the maximum unsecured loan a Branch Manager can approve?**
$25,000. Above $25,000, the application escalates to T2 (Regional Credit Officer).

**Q2. What's the maximum unsecured loan a Regional Credit Officer can approve?**
$100,000.

**Q3. What's the maximum unsecured loan the Credit Committee can approve?**
$500,000. Above $500,000, the Board Credit Committee (T4) is required.

**Q4. What's the secured-loan cap at each tier?**
4× the unsecured cap: $100,000 (T1), $400,000 (T2), $2,000,000 (T3), and anything above for T4.

**Q5. How does aggregation work for a customer with multiple facilities?**
Aggregate exposure across all facilities — including joint, guarantor, and mixed secured/unsecured — determines the tier. A small new loan to a large-exposure customer can still require T3 or T4.

**Q6. What's the DTI ceiling for an unsecured personal loan?**
36%. Same as the Credit Risk Assessment page.

**Q7. What's the DTI ceiling for a QM mortgage?**
43%. Same as the Credit Risk Assessment page and the Credit Policy Manual.

**Q8. How are exceptions approved?**
One tier above the normal authority. A T1 exception requires T2 approval; a T2 exception requires T3.

**Q9. What's the Bank's annual exception rate ceiling?**
5% of all originations. Approaching the ceiling triggers a portfolio review.

**Q10. What's the maximum unsecured exposure to a single Borrower across all facilities?**
$250,000. Above that, additional credit must be secured.

**Q11. What's the maximum QM mortgage exposure to a single Borrower?**
$2,000,000. Jumbo treatment begins at the 2026 conforming-loan limit of $766,550.

**Q12. Can a tier approve credit for a Related Party?**
No. A Related Party's file is routed to the next-higher tier regardless of amount.

## Cross-References

This page and [Credit-Risk-Assessment-Guidelines.md](Credit-Risk-Assessment-Guidelines.md) form a pair — credit gates here, approval authority there. The 36% and 43% DTI ceilings appear in both pages with identical values. The credit decision tree diagram is embedded in both pages and in the Credit Policy Manual. Applicant identity and CDD risk rating are documented in [KYC-Customer-Onboarding-Policy.md](KYC-Customer-Onboarding-Policy.md). Complaints from declined applicants are handled under [Customer-Complaint-Handling-Policy.md](Customer-Complaint-Handling-Policy.md).

## Attachments

- [attachments/credit-policy-manual.pdf](attachments/credit-policy-manual.pdf) — Section 3 of the manual restates the tier matrix.
- [attachments/credit-officer-decision-framework.docx](attachments/credit-officer-decision-framework.docx) — Desk-level companion with escalation triggers and the Exception Log template.
- [attachments/credit-decision-tree.png](attachments/credit-decision-tree.png) — The decision-tree diagram embedded above.

## See also

- [Credit Risk Assessment Guidelines](Credit-Risk-Assessment-Guidelines.md)
- [KYC Customer Onboarding Policy](KYC-Customer-Onboarding-Policy.md)
- [Customer Complaint Handling Policy](Customer-Complaint-Handling-Policy.md)
- [Home](Home.md)
