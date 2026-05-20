"""Generate the 3 PDFs for the Northvale Demo Bank wiki.

Outputs to attachments/:
  - compliance-handbook-v8.pdf            (~5 pages, embeds onboarding-flow + aml-escalation)
  - regulatory-circular-2026-02.pdf       (~5 pages, embeds sanctions-screening-flow)
  - credit-policy-manual.pdf              (~10 pages, embeds credit-decision-tree)

All content is FICTIONAL for the GenAI RAG capstone demo.
"""
from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ATTACH = Path(__file__).resolve().parent.parent / "docs" / "attachments"
ATTACH.mkdir(parents=True, exist_ok=True)

NAVY = colors.HexColor("#1a237e")
INDIGO = colors.HexColor("#3949ab")
TEAL = colors.HexColor("#00897b")
GREY = colors.HexColor("#546e7a")
LIGHT = colors.HexColor("#eceff1")

styles = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=styles["Heading1"], textColor=NAVY, spaceAfter=12, fontSize=18)
H2 = ParagraphStyle("H2", parent=styles["Heading2"], textColor=INDIGO, spaceAfter=8, fontSize=14)
H3 = ParagraphStyle("H3", parent=styles["Heading3"], textColor=TEAL, spaceAfter=6, fontSize=12)
BODY = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontSize=10.5,
    leading=14,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
)
SMALL = ParagraphStyle("Small", parent=BODY, fontSize=9, textColor=GREY, alignment=TA_CENTER)
COVER_TITLE = ParagraphStyle(
    "CoverTitle",
    parent=styles["Title"],
    textColor=NAVY,
    fontSize=26,
    alignment=TA_CENTER,
    spaceAfter=24,
)
COVER_SUB = ParagraphStyle(
    "CoverSub",
    parent=BODY,
    fontSize=14,
    textColor=INDIGO,
    alignment=TA_CENTER,
    spaceAfter=12,
)


def _header_footer(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 8)
    canv.setFillColor(GREY)
    canv.drawString(0.75 * inch, 10.6 * inch, "Northvale Demo Bank - FICTIONAL FOR DEMONSTRATION")
    canv.drawRightString(7.75 * inch, 10.6 * inch, doc.title)
    canv.drawCentredString(4.25 * inch, 0.4 * inch, f"Page {canv.getPageNumber()}")
    canv.setStrokeColor(LIGHT)
    canv.setLineWidth(0.6)
    canv.line(0.75 * inch, 10.5 * inch, 7.75 * inch, 10.5 * inch)
    canv.restoreState()


def _build(filename: str, title: str, story):
    out = ATTACH / filename
    doc = SimpleDocTemplate(
        str(out),
        pagesize=LETTER,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=1.0 * inch,
        bottomMargin=0.75 * inch,
        title=title,
        author="Northvale Demo Bank (fictional)",
    )
    doc.build(story, onFirstPage=_header_footer, onLaterPages=_header_footer)
    print(f"  wrote {out.relative_to(ATTACH.parent)}")


def _para(text: str, style=BODY) -> Paragraph:
    return Paragraph(text, style)


def _img(name: str, max_width_in: float = 6.0) -> Image:
    img = Image(str(ATTACH / name))
    aspect = img.imageHeight / img.imageWidth
    img.drawWidth = max_width_in * inch
    img.drawHeight = max_width_in * inch * aspect
    img.hAlign = "CENTER"
    return img


def _table(data, col_widths=None):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, 0), 10),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("TOPPADDING", (0, 0), (-1, 0), 6),
                ("BACKGROUND", (0, 1), (-1, -1), LIGHT),
                ("FONTSIZE", (0, 1), (-1, -1), 9.5),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.4, GREY),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 1), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
            ]
        )
    )
    return t


# ---------------------------------------------------------------------------
# 1. Compliance Handbook v8
# ---------------------------------------------------------------------------
def compliance_handbook():
    s = []
    s.append(Spacer(1, 1.2 * inch))
    s.append(_para("Northvale Demo Bank", COVER_TITLE))
    s.append(_para("Compliance Handbook", COVER_SUB))
    s.append(_para("Version 8.0 - Effective January 1, 2026", COVER_SUB))
    s.append(Spacer(1, 1.0 * inch))
    s.append(
        _para(
            "This Handbook consolidates the Bank's core compliance obligations for retail banking "
            "operations, including Customer Identification (CIP), Customer Due Diligence (CDD), "
            "Enhanced Due Diligence (EDD), and the Anti-Money-Laundering (AML) monitoring program. "
            "It supersedes Version 7.2 issued July 1, 2024.",
            BODY,
        )
    )
    s.append(Spacer(1, 0.6 * inch))
    s.append(_para("FICTIONAL DOCUMENT - GenAI RAG capstone demo", SMALL))
    s.append(PageBreak())

    # TOC
    s.append(_para("Table of Contents", H1))
    s.append(
        _table(
            [
                ["Section", "Title", "Page"],
                ["1", "KYC / Customer Identification Program (CIP)", "2"],
                ["2", "Customer Due Diligence and Risk Rating", "3"],
                ["3", "Anti-Money-Laundering Monitoring", "4"],
                ["4", "SAR and CTR Filing Obligations", "5"],
                ["5", "Version History and Sign-off", "5"],
            ],
            col_widths=[0.8 * inch, 4.6 * inch, 0.7 * inch],
        )
    )
    s.append(Spacer(1, 0.4 * inch))
    s.append(
        _para(
            "The handbook is organized into five chapters. Chapter 1 covers identity verification for "
            "new customers at account opening. Chapter 2 introduces the CDD risk-rating model that drives "
            "review cadence. Chapter 3 sets out the rules-based and analyst-led AML monitoring program. "
            "Chapter 4 describes SAR and CTR filing obligations. Chapter 5 is the version history.",
            BODY,
        )
    )
    s.append(PageBreak())

    # Chapter 1 - KYC / CIP
    s.append(_para("1. KYC / Customer Identification Program (CIP)", H1))
    s.append(
        _para(
            "The Bank shall complete Customer Identification Procedures (CIP) for every new account "
            "within thirty (30) calendar days of the Account Opening Date. CIP requires collection and "
            "verification of: (a) legal name, (b) date of birth, (c) residential address, and "
            "(d) a government-issued identification number (Social Security Number for U.S. persons; "
            "passport or other approved identification for non-U.S. persons).",
            BODY,
        )
    )
    s.append(
        _para(
            "Where verification cannot be completed within the thirty-day window, the relationship "
            "shall be escalated to the Branch Manager and, if still unresolved at day sixty, the "
            "account shall be restricted and closed in line with the Account Closure Procedure.",
            BODY,
        )
    )
    s.append(_para("Onboarding Flow Diagram", H3))
    s.append(_img("onboarding-flow.png", max_width_in=5.8))
    s.append(
        _para(
            "Figure 1.1 - Onboarding flow. The diagram shows the four sequential gates an applicant "
            "passes through (Application Received, Identity Verification, Sanctions/PEP Screening, "
            "and CDD Risk Rating), followed by a High-Risk decision branch that routes the file "
            "either to Enhanced Due Diligence with senior approval or to the Standard Approval workflow. "
            "All approved files terminate in Account Opened plus Ongoing Monitoring scheduling.",
            BODY,
        )
    )
    s.append(PageBreak())

    # Chapter 2 - CDD
    s.append(_para("2. Customer Due Diligence and Risk Rating", H1))
    s.append(
        _para(
            "At account opening the Bank shall assign each Customer a CDD Risk Rating of Low, Medium, "
            "or High. The rating drives the periodic review cadence and the depth of documentation "
            "required at each review.",
            BODY,
        )
    )
    s.append(
        _para(
            "The table below sets out the review cadence and documentation requirements by risk rating. "
            "Low-risk customers are reviewed every 24 months and require refresh of basic identification "
            "and address. Medium-risk customers are reviewed every 12 months with source-of-funds "
            "narrative. High-risk customers receive Enhanced Due Diligence every 6 months with senior "
            "compliance sign-off.",
            BODY,
        )
    )
    s.append(
        _table(
            [
                ["Risk Rating", "Review Cadence", "Documentation"],
                ["Low (standard)", "Every 24 months", "ID, address, occupation"],
                ["Medium", "Every 12 months", "Above + source of funds narrative"],
                ["High (EDD)", "Every 6 months", "Above + senior compliance sign-off + ownership tree"],
            ],
            col_widths=[1.4 * inch, 1.6 * inch, 3.1 * inch],
        )
    )
    s.append(Spacer(1, 0.2 * inch))
    s.append(
        _para(
            "In summary the cadence shortens as risk increases, and the documentation required at each "
            "touchpoint deepens correspondingly. The 24 / 12 / 6 month cycle is the canonical reference "
            "across all retail banking products and is cited in both the KYC policy and the AML "
            "ongoing-monitoring procedure.",
            BODY,
        )
    )
    s.append(PageBreak())

    # Chapter 3 - AML
    s.append(_para("3. Anti-Money-Laundering Monitoring", H1))
    s.append(
        _para(
            "The Bank operates a hybrid AML monitoring program combining rules-based alerts (velocity, "
            "structuring, cross-border patterns) with quarterly analyst-led reviews. Every alert is "
            "triaged by a Level 1 (L1) Analyst within two (2) business days of generation. Alerts not "
            "closed at L1 are escalated to a Level 2 (L2) Investigator who has ten (10) business days "
            "to complete the case file.",
            BODY,
        )
    )
    s.append(_para("AML Escalation Process", H3))
    s.append(_img("aml-escalation-process.png", max_width_in=5.8))
    s.append(
        _para(
            "Figure 3.1 - AML escalation. The diagram traces an alert from the monitoring system through "
            "L1 triage and an initial reasonable-suspicion decision. Alerts cleared at L1 are closed and "
            "documented. Alerts that meet the reasonable-suspicion threshold escalate to an L2 Investigator "
            "who decides whether to file a SAR; SARs are reviewed and signed off by the BSA Officer. "
            "Parallel CTR filing is triggered for cash transactions exceeding $10,000.",
            BODY,
        )
    )
    s.append(PageBreak())

    # Chapter 4 - SAR / CTR
    s.append(_para("4. SAR and CTR Filing Obligations", H1))
    s.append(
        _para(
            "Suspicious Activity Reports (SARs) shall be filed with FinCEN within thirty (30) calendar "
            "days of the date the Bank initially detects facts that may constitute a basis for filing. "
            "Where no suspect has been identified, the deadline may be extended to sixty (60) calendar "
            "days. Currency Transaction Reports (CTRs) shall be filed within fifteen (15) calendar days "
            "of any cash transaction (or aggregated same-day transactions) exceeding ten thousand "
            "dollars ($10,000).",
            BODY,
        )
    )
    s.append(
        _para(
            "Filing deadlines are summarized in the table below. The 30/60-day SAR window and the "
            "$10,000 CTR threshold are referenced consistently in the AML Procedures wiki page and the "
            "Complaint Handling policy (for complaints that surface suspected financial crime).",
            BODY,
        )
    )
    s.append(
        _table(
            [
                ["Report", "Threshold", "Filing Window"],
                ["SAR (with suspect)", "Reasonable suspicion", "30 calendar days"],
                ["SAR (no suspect)", "Reasonable suspicion", "60 calendar days"],
                ["CTR", "Cash > $10,000 same day", "15 calendar days"],
            ],
            col_widths=[1.7 * inch, 2.0 * inch, 2.0 * inch],
        )
    )
    s.append(Spacer(1, 0.2 * inch))

    # Chapter 5 - Version history
    s.append(_para("5. Version History and Sign-off", H1))
    s.append(
        _table(
            [
                ["Version", "Effective Date", "Notes"],
                ["8.0", "January 1, 2026", "Aligned 24/12/6 CDD cadence; restated SAR/CTR windows"],
                ["7.2", "July 1, 2024", "Added cross-border velocity rules"],
                ["7.1", "January 1, 2024", "Updated CIP for digital onboarding"],
                ["7.0", "April 1, 2023", "Reorganized chapters; introduced EDD"],
            ],
            col_widths=[0.9 * inch, 1.4 * inch, 3.5 * inch],
        )
    )
    s.append(Spacer(1, 0.3 * inch))
    s.append(
        _para(
            "Approved by the Northvale Demo Bank Chief Compliance Officer, December 15, 2025. This "
            "Handbook is fictional and exists solely to support a GenAI RAG capstone demonstration.",
            BODY,
        )
    )

    _build("compliance-handbook-v8.pdf", "Compliance Handbook v8", s)


# ---------------------------------------------------------------------------
# 2. Regulatory Circular 2026-02
# ---------------------------------------------------------------------------
def regulatory_circular():
    s = []
    s.append(Spacer(1, 0.5 * inch))
    s.append(_para("Northvale Demo Bank", COVER_TITLE))
    s.append(_para("Regulatory Circular 2026-02", COVER_SUB))
    s.append(_para("Sanctions Screening Threshold Update", COVER_SUB))
    s.append(_para("Issued: February 14, 2026 - Effective: March 1, 2026", COVER_SUB))
    s.append(Spacer(1, 0.4 * inch))
    s.append(
        _para(
            "To: All retail branches, the Customer Onboarding Operations team, and the Financial Crime "
            "Operations team. From: Office of the Chief Compliance Officer. This circular updates the "
            "fuzzy-match threshold used in real-time sanctions screening and clarifies the four-business-"
            "hour service level for reviewing potential matches.",
            BODY,
        )
    )
    s.append(PageBreak())

    s.append(_para("1. Background", H1))
    s.append(
        _para(
            "Following a Q4 2025 calibration exercise, the Financial Crime Operations team observed a "
            "false-positive rate of approximately 18% at the previous similarity threshold. This "
            "circular adjusts the Jaro-Winkler similarity floor from 80% to 85% and reaffirms that all "
            "potential matches must be cleared or escalated within four (4) business hours of alert "
            "generation.",
            BODY,
        )
    )
    s.append(_para("2. Updated Screening Flow", H1))
    s.append(_img("sanctions-screening-flow.png", max_width_in=5.6))
    s.append(
        _para(
            "Figure 2.1 - Sanctions screening flow. The diagram shows inbound names being normalized "
            "and transliterated before fuzzy-matching against the OFAC SDN, UN consolidated, and EU "
            "consolidated lists. A similarity score at or above 85% generates an alert routed to a "
            "Tier 1 Analyst, who must reach a true-match / false-positive decision within four business "
            "hours. True matches trigger transaction blocking, fund freezing, and an OFAC report within "
            "ten calendar days.",
            BODY,
        )
    )
    s.append(PageBreak())

    s.append(_para("3. Effective Date Schedule", H1))
    s.append(
        _para(
            "The table below sets out the effective-date schedule for the three populations affected by "
            "this circular. New onboarding flows transition immediately on March 1. Existing customer "
            "rescreening occurs in the following two months, and legacy bulk batches roll over in April.",
            BODY,
        )
    )
    s.append(
        _table(
            [
                ["Population", "Cutover Date", "Owner"],
                ["New onboarding (real-time)", "March 1, 2026", "Customer Onboarding Ops"],
                ["Existing customer rescreening", "March 15 - April 30, 2026", "Financial Crime Ops"],
                ["Legacy batch jobs", "April 30, 2026", "Sanctions Technology"],
            ],
            col_widths=[2.3 * inch, 1.9 * inch, 1.8 * inch],
        )
    )
    s.append(Spacer(1, 0.2 * inch))
    s.append(
        _para(
            "All three populations must be operating at the new 85% threshold by April 30, 2026. "
            "Branch managers shall confirm rescreening completion to their Regional Compliance Officer "
            "by May 7, 2026.",
            BODY,
        )
    )
    s.append(PageBreak())

    s.append(_para("4. Politically Exposed Persons (PEPs)", H1))
    s.append(
        _para(
            "This circular does not change PEP screening, which continues to operate against a daily-"
            "refreshed vendor list with the same four-business-hour match-review SLA used for sanctions "
            "matches. PEP screening procedures are documented in the Sanctions Screening Procedures "
            "wiki page and cross-referenced from the KYC Customer Onboarding Policy.",
            BODY,
        )
    )
    s.append(
        _para(
            "Where a PEP match coincides with a sanctions match (a 'compound match'), the case shall "
            "be routed directly to a Tier 2 Sanctions Investigator and the four-business-hour SLA "
            "applies to the first analyst review rather than to final disposition.",
            BODY,
        )
    )
    s.append(PageBreak())

    s.append(_para("5. Appendix - Defined Terms", H1))
    s.append(
        _table(
            [
                ["Term", "Definition"],
                ["SDN List", "Specially Designated Nationals list maintained by OFAC"],
                ["Jaro-Winkler", "String similarity metric used by the Bank's screening engine"],
                ["True Match", "A potential match confirmed to be the listed individual or entity"],
                ["False Positive", "A potential match cleared after analyst review"],
                ["Compound Match", "Concurrent PEP + sanctions match on the same name"],
            ],
            col_widths=[1.7 * inch, 4.3 * inch],
        )
    )
    s.append(Spacer(1, 0.3 * inch))
    s.append(
        _para(
            "Questions on this circular should be directed to the Office of the Chief Compliance "
            "Officer. This document is fictional and exists for GenAI RAG demonstration purposes only.",
            BODY,
        )
    )

    _build("regulatory-circular-2026-02.pdf", "Regulatory Circular 2026-02", s)


# ---------------------------------------------------------------------------
# 3. Credit Policy Manual (~10 pages)
# ---------------------------------------------------------------------------
def credit_policy_manual():
    s = []
    # Cover
    s.append(Spacer(1, 1.4 * inch))
    s.append(_para("Northvale Demo Bank", COVER_TITLE))
    s.append(_para("Credit Policy Manual", COVER_SUB))
    s.append(_para("Effective January 1, 2026", COVER_SUB))
    s.append(Spacer(1, 1.0 * inch))
    s.append(
        _para(
            "This Manual establishes the Bank's lending principles, scoring criteria, approval tiers, "
            "exception handling, and monitoring obligations for all retail credit products including "
            "unsecured personal loans, residential mortgages, home equity lines of credit (HELOCs), "
            "and auto loans.",
            BODY,
        )
    )
    s.append(PageBreak())

    # TOC
    s.append(_para("Table of Contents", H1))
    s.append(
        _table(
            [
                ["Section", "Title", "Page"],
                ["1", "Credit Principles", "3"],
                ["2", "Scoring Criteria", "4"],
                ["3", "Loan Approval Tiers", "5"],
                ["4", "Credit Decision Tree", "6"],
                ["5", "Exception Handling", "7"],
                ["6", "Ongoing Portfolio Monitoring", "8"],
                ["7", "Glossary", "9"],
                ["8", "Sign-off", "10"],
            ],
            col_widths=[0.9 * inch, 4.5 * inch, 0.7 * inch],
        )
    )
    s.append(PageBreak())

    # 1. Principles
    s.append(_para("1. Credit Principles", H1))
    s.append(
        _para(
            "The Bank shall extend credit only where the Borrower demonstrates the willingness and "
            "capacity to repay. Willingness is evidenced by credit history (FICO score, derogatory "
            "items, payment patterns). Capacity is evidenced by income, employment stability, and "
            "Debt-to-Income (DTI) ratio. Collateral is considered a secondary repayment source and "
            "shall not substitute for inadequate capacity.",
            BODY,
        )
    )
    s.append(
        _para(
            "Every credit decision shall be documented with a written rationale that addresses (a) the "
            "Borrower's character and credit history, (b) capacity as measured by income and DTI, "
            "(c) collateral coverage as measured by Loan-to-Value (LTV), and (d) any compensating "
            "factors. No Loan Officer may originate credit outside their delegated authority.",
            BODY,
        )
    )
    s.append(PageBreak())

    # 2. Scoring criteria
    s.append(_para("2. Scoring Criteria", H1))
    s.append(
        _para(
            "The table below sets out minimum scoring criteria by product. The unsecured personal loan "
            "minimum FICO is 660 with a DTI ceiling of 36%. Residential mortgage origination requires "
            "a minimum FICO of 620 and complies with Qualified Mortgage rules including the 43% DTI "
            "ceiling. Prime auto loans require a minimum FICO of 700 and a maximum LTV of 110% of "
            "invoice price.",
            BODY,
        )
    )
    s.append(
        _table(
            [
                ["Product", "Min FICO", "Max DTI", "Max LTV", "Notes"],
                ["Unsecured personal loan", "660", "36%", "n/a", "Co-signer required below 700 FICO"],
                ["Residential mortgage (QM)", "620", "43%", "80% / 95% w/ PMI", "QM safe-harbor"],
                ["HELOC", "680", "43%", "90%", "Combined LTV including 1st lien"],
                ["Prime auto loan", "700", "40%", "110% invoice", "Max term 72 months"],
                ["Subprime auto loan", "580", "45%", "120% invoice", "Senior approval required"],
            ],
            col_widths=[1.7 * inch, 0.7 * inch, 0.7 * inch, 1.1 * inch, 1.8 * inch],
        )
    )
    s.append(Spacer(1, 0.15 * inch))
    s.append(
        _para(
            "Applications that fall short of the table's minimums may proceed only as documented "
            "exceptions per Section 5. The DTI ceilings of 36% (unsecured) and 43% (QM mortgage) are "
            "the canonical figures cited in both the Credit Risk Assessment Guidelines and the Loan "
            "Approval Thresholds wiki pages.",
            BODY,
        )
    )
    s.append(PageBreak())

    # 3. Tiers
    s.append(_para("3. Loan Approval Tiers", H1))
    s.append(
        _para(
            "Approval authority is delegated in four tiers. Tier 1 Branch Managers may approve "
            "unsecured credit up to $25,000. Tier 2 Regional Credit Officers may approve up to $100,000. "
            "Tier 3 Credit Committee approval is required up to $500,000. Any unsecured exposure above "
            "$500,000 requires Tier 4 Board Credit Committee approval. Secured exposure tiers are 4x "
            "the unsecured limits at each level.",
            BODY,
        )
    )
    s.append(
        _table(
            [
                ["Tier", "Authority", "Unsecured Cap", "Secured Cap"],
                ["T1", "Branch Manager", "$25,000", "$100,000"],
                ["T2", "Regional Credit Officer", "$100,000", "$400,000"],
                ["T3", "Credit Committee", "$500,000", "$2,000,000"],
                ["T4", "Board Credit Committee", "Above $500,000", "Above $2,000,000"],
            ],
            col_widths=[0.7 * inch, 2.1 * inch, 1.5 * inch, 1.5 * inch],
        )
    )
    s.append(Spacer(1, 0.15 * inch))
    s.append(
        _para(
            "Each tier-level approver shall sign a credit memorandum referencing the FICO, DTI, LTV, "
            "and any compensating factors. Approvers may not approve credit for a Related Party as "
            "defined in Section 7.",
            BODY,
        )
    )
    s.append(PageBreak())

    # 4. Decision tree
    s.append(_para("4. Credit Decision Tree", H1))
    s.append(_img("credit-decision-tree.png", max_width_in=5.8))
    s.append(
        _para(
            "Figure 4.1 - Credit decision tree for unsecured personal loans. The diagram shows the "
            "initial FICO and DTI gate (FICO >= 660 and DTI <= 36%); applicants failing the gate are "
            "declined or referred to a secured product. Approved applicants are then routed by loan "
            "amount through the four approval tiers - Branch Manager, Regional Credit Officer, Credit "
            "Committee, or Board Credit Committee.",
            BODY,
        )
    )
    s.append(PageBreak())

    # 5. Exception handling
    s.append(_para("5. Exception Handling", H1))
    s.append(
        _para(
            "An exception is any credit decision that deviates from the scoring criteria in Section 2 "
            "or the tier limits in Section 3. Every exception shall be (a) approved one tier above the "
            "tier that would normally hold authority, (b) documented in the Exception Log, and "
            "(c) reviewed in aggregate by the Credit Committee on a quarterly basis. The Bank's annual "
            "exception rate ceiling is 5% of all originations.",
            BODY,
        )
    )
    s.append(
        _para(
            "Permissible compensating factors include: documented liquid reserves greater than twelve "
            "months of debt service, a guarantor with a minimum FICO of 740, or a loan-to-value ratio "
            "below 60% on a secured product. Compensating factors shall be evidenced in the credit "
            "file and referenced in the credit memorandum.",
            BODY,
        )
    )
    s.append(PageBreak())

    # 6. Monitoring
    s.append(_para("6. Ongoing Portfolio Monitoring", H1))
    s.append(
        _para(
            "The Bank shall monitor every loan continuously for repayment performance, collateral "
            "value (for secured loans), and Borrower distress indicators. Loans become delinquent on "
            "day 16 (after the 15-day grace period) and shall be classified as non-performing at day 90. "
            "Loans 30 days delinquent trigger an outbound collections call; loans 60 days delinquent "
            "are referred to the workout team.",
            BODY,
        )
    )
    s.append(
        _table(
            [
                ["Delinquency", "Status", "Action"],
                ["1 - 15 days", "Grace period", "No fee, no action"],
                ["16 - 29 days", "Delinquent", "Late fee ($35); courtesy call"],
                ["30 - 59 days", "Past due", "Collections call; payment plan offered"],
                ["60 - 89 days", "Seriously past due", "Workout referral; credit bureau update"],
                ["90+ days", "Non-performing", "Charge-off review; legal referral"],
            ],
            col_widths=[1.4 * inch, 1.6 * inch, 3.0 * inch],
        )
    )
    s.append(Spacer(1, 0.15 * inch))
    s.append(
        _para(
            "The 15-day grace period, $35 late fee, and 90-day non-performing threshold are also "
            "cited in the Customer Complaint Handling Policy where they intersect with disputed-fee "
            "complaints.",
            BODY,
        )
    )
    s.append(PageBreak())

    # 7. Glossary
    s.append(_para("7. Glossary", H1))
    s.append(
        _table(
            [
                ["Term", "Definition"],
                ["FICO", "Standardized U.S. consumer credit score"],
                ["DTI", "Debt-to-Income ratio - monthly debt obligations / gross monthly income"],
                ["LTV", "Loan-to-Value ratio - loan amount / appraised collateral value"],
                ["QM", "Qualified Mortgage - meets ATR rule, 43% DTI ceiling, no risky features"],
                ["HELOC", "Home Equity Line of Credit"],
                ["PMI", "Private Mortgage Insurance - required when LTV exceeds 80%"],
                ["Related Party", "Bank officer, director, or immediate family member"],
                ["Workout", "Negotiated restructuring of distressed loans"],
            ],
            col_widths=[1.5 * inch, 4.5 * inch],
        )
    )
    s.append(PageBreak())

    # 8. Sign-off
    s.append(_para("8. Sign-off", H1))
    s.append(
        _para(
            "This Manual was approved by the Northvale Demo Bank Credit Committee on December 18, 2025 "
            "and supersedes all prior versions of the Credit Policy Manual. The next scheduled review "
            "is December 2026.",
            BODY,
        )
    )
    s.append(Spacer(1, 0.5 * inch))
    s.append(
        _para(
            "Northvale Demo Bank does not exist. This Manual is fictional and is provided exclusively "
            "for the GenAI RAG capstone demonstration.",
            SMALL,
        )
    )

    _build("credit-policy-manual.pdf", "Credit Policy Manual", s)


def main():
    print("Generating PDFs...")
    compliance_handbook()
    regulatory_circular()
    credit_policy_manual()
    print("Done.")


if __name__ == "__main__":
    main()
