"""Generate the 2 DOCX files for the Northvale Demo Bank wiki.

Outputs to attachments/:
  - credit-officer-decision-framework.docx          (~5 pages)
  - quarterly-compliance-update-q1-2026.docx        (~3 pages)

All content is FICTIONAL for the GenAI RAG capstone demo.
"""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt, RGBColor

ATTACH = Path(__file__).resolve().parent.parent / "docs" / "attachments"
ATTACH.mkdir(parents=True, exist_ok=True)

NAVY = RGBColor(0x1A, 0x23, 0x7E)
INDIGO = RGBColor(0x39, 0x49, 0xAB)
TEAL = RGBColor(0x00, 0x89, 0x7B)
GREY = RGBColor(0x54, 0x6E, 0x7A)


def _set_heading(doc: Document, text: str, level: int = 1, color: RGBColor = NAVY):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = color
    return h


def _footer_para(doc: Document, text: str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = GREY


def _set_doc_header(doc: Document, title: str):
    section = doc.sections[0]
    header = section.header
    p = header.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(f"Northvale Demo Bank - {title} - FICTIONAL FOR DEMONSTRATION")
    r.italic = True
    r.font.size = Pt(8.5)
    r.font.color.rgb = GREY


def _table(doc: Document, header: list[str], rows: list[list[str]]):
    tbl = doc.add_table(rows=1 + len(rows), cols=len(header))
    tbl.style = "Table Grid"
    hdr_cells = tbl.rows[0].cells
    for i, h in enumerate(header):
        hdr_cells[i].text = h
        for paragraph in hdr_cells[i].paragraphs:
            for run in paragraph.runs:
                run.bold = True
                run.font.color.rgb = NAVY
                run.font.size = Pt(10)
    for ridx, row in enumerate(rows, start=1):
        cells = tbl.rows[ridx].cells
        for cidx, val in enumerate(row):
            cells[cidx].text = val
            for paragraph in cells[cidx].paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(10)
            cells[cidx].vertical_alignment = WD_ALIGN_VERTICAL.TOP
    return tbl


# ---------------------------------------------------------------------------
# 1. Credit Officer Decision Framework (~5 pages)
# ---------------------------------------------------------------------------
def credit_officer_decision_framework():
    doc = Document()
    _set_doc_header(doc, "Credit Officer Decision Framework")

    _set_heading(doc, "Credit Officer Decision Framework", level=0, color=NAVY)
    p = doc.add_paragraph()
    r = p.add_run("Northvale Demo Bank - Operations Procedure - Effective January 1, 2026")
    r.italic = True
    r.font.color.rgb = INDIGO
    doc.add_paragraph(
        "This Framework is the desk-level companion to the Credit Policy Manual. It tells the credit "
        "officer (a) how to read an application packet, (b) what facts to verify before approval, "
        "(c) how to apply the four-tier approval matrix, (d) when to escalate, and (e) how to log an "
        "exception. The Framework binds every credit officer in the Bank's retail lending operation."
    )

    # 1. Role overview
    _set_heading(doc, "1. Role Overview", level=1)
    doc.add_paragraph(
        "A Credit Officer is responsible for arriving at a documented credit decision (Approve, "
        "Decline, Counter-Offer, or Refer) on every retail loan application routed to their queue. "
        "Decisions shall be reached within five (5) business days of receipt of a complete packet. "
        "Incomplete packets are returned to the originating branch within one (1) business day."
    )
    doc.add_paragraph(
        "Every decision shall produce three artifacts: (a) the credit memorandum that captures FICO, "
        "DTI, LTV, and the rationale; (b) the approval signature in the Loan Origination System (LOS); "
        "and (c) a customer-facing decision letter sent within two (2) business days of decision."
    )

    # 2. Decision authority matrix
    _set_heading(doc, "2. Decision Authority Matrix", level=1)
    doc.add_paragraph(
        "The Bank operates four approval tiers. The tier required for any given application is the "
        "lowest tier whose unsecured cap covers the proposed exposure. Where a single Borrower has "
        "multiple facilities, aggregate exposure determines tier. The matrix below is the operational "
        "restatement of the same tiers documented in the Credit Policy Manual and the Loan Approval "
        "Thresholds wiki page."
    )
    _table(
        doc,
        ["Tier", "Authority", "Unsecured Cap", "Secured Cap", "Escalation Trigger"],
        [
            ["T1", "Branch Manager", "$25,000", "$100,000", "DTI > 36% or exception requested"],
            ["T2", "Regional Credit Officer", "$100,000", "$400,000", "Aggregate exposure > $100k"],
            ["T3", "Credit Committee", "$500,000", "$2,000,000", "Aggregate exposure > $500k"],
            ["T4", "Board Credit Committee", "Above $500,000", "Above $2,000,000", "Any exposure > T3 cap"],
        ],
    )
    doc.add_paragraph(
        "Approvers may not approve credit for themselves, an immediate family member, or any Related "
        "Party as defined in the Credit Policy Manual glossary. The next-higher tier shall handle "
        "Related Party files in all cases."
    )

    # 3. Escalation scenarios
    _set_heading(doc, "3. Escalation Scenarios", level=1)
    doc.add_paragraph(
        "Credit officers shall escalate immediately, regardless of loan amount, when any of the "
        "following are present:"
    )
    for bullet in [
        "FICO score is below the product minimum (660 unsecured, 620 mortgage, 700 prime auto).",
        "DTI exceeds the product ceiling (36% unsecured, 43% QM mortgage).",
        "The applicant or any beneficial owner is flagged as a Politically Exposed Person (PEP) or appears on a sanctions list.",
        "Any element of the income documentation is inconsistent with stated income.",
        "The applicant has filed a complaint against the Bank that remains unresolved at the time of application.",
        "The application is from a Related Party of any Bank employee.",
    ]:
        doc.add_paragraph(bullet, style="List Bullet")

    doc.add_paragraph(
        "Escalations to Tier 2 shall be routed via the LOS escalation queue with a one-paragraph "
        "rationale. Escalations to Tier 3 or Tier 4 shall also include a written exception memorandum."
    )

    # 4. Exception log template
    _set_heading(doc, "4. Exception Log Template", level=1)
    doc.add_paragraph(
        "Every exception shall be logged using the template below. The Exception Log is reviewed "
        "quarterly by the Credit Committee and is subject to the Bank's 5% aggregate exception ceiling "
        "described in Section 5 of the Credit Policy Manual."
    )
    _table(
        doc,
        ["Field", "Description"],
        [
            ["Application ID", "LOS application identifier"],
            ["Date", "Date of exception approval"],
            ["Borrower Name", "Full legal name"],
            ["Product", "Unsecured / mortgage / HELOC / auto"],
            ["Exception Type", "FICO / DTI / LTV / amount / other"],
            ["Standard Value", "The policy threshold being relaxed"],
            ["Actual Value", "The applicant's value"],
            ["Compensating Factors", "Documented mitigants"],
            ["Approving Tier", "Tier and approver name"],
            ["Quarterly Review Outcome", "Filled at Credit Committee review"],
        ],
    )

    # 5. Sign-off
    _set_heading(doc, "5. Sign-off and Acknowledgment", level=1)
    doc.add_paragraph(
        "Every credit officer shall acknowledge this Framework annually as part of the Bank's "
        "compliance training. Signed acknowledgments are retained by the Office of the Chief "
        "Compliance Officer for five (5) years. The Framework will next be reviewed in December 2026."
    )
    doc.add_paragraph(
        "Approved by: Chief Credit Officer, Northvale Demo Bank. Approval date: December 20, 2025."
    )

    _footer_para(
        doc,
        "Northvale Demo Bank is fictional. This document exists solely for the GenAI RAG capstone demonstration.",
    )

    out = ATTACH / "credit-officer-decision-framework.docx"
    doc.save(out)
    print(f"  wrote {out.relative_to(ATTACH.parent)}")


# ---------------------------------------------------------------------------
# 2. Quarterly Compliance Update Q1 2026 (~3 pages)
# ---------------------------------------------------------------------------
def quarterly_compliance_update():
    doc = Document()
    _set_doc_header(doc, "Quarterly Compliance Update Q1 2026")

    _set_heading(doc, "Quarterly Compliance Update", level=0, color=NAVY)
    p = doc.add_paragraph()
    r = p.add_run("Q1 2026 - Issued March 31, 2026 - Office of the Chief Compliance Officer")
    r.italic = True
    r.font.color.rgb = INDIGO

    # 1. Executive summary
    _set_heading(doc, "1. Executive Summary", level=1)
    doc.add_paragraph(
        "Q1 2026 closed with the Bank in good standing across all retail compliance pillars. KYC "
        "completion rate at day 30 reached 98.4% (target: 98%). SAR filings increased 6% quarter on "
        "quarter, consistent with the new cross-border velocity rules. The 85% Jaro-Winkler threshold "
        "introduced by Regulatory Circular 2026-02 went live on March 1 with no operational incidents. "
        "Customer complaint resolution time averaged 18 calendar days against a 30-day target."
    )

    # 2. Regulatory updates
    _set_heading(doc, "2. Regulatory Updates", level=1)
    doc.add_paragraph(
        "Three regulatory items were addressed in Q1. First, Regulatory Circular 2026-02 (sanctions "
        "threshold update) was rolled out across new onboarding, existing customer rescreening, and "
        "legacy batches. Second, the annual update to the Compliance Handbook (Version 8.0) was "
        "distributed effective January 1. Third, the Bank refreshed the BSA Officer designation "
        "letter following the departure of the prior officer in late December."
    )

    _table(
        doc,
        ["Item", "Status", "Owner"],
        [
            ["Circular 2026-02 rollout", "Complete on Mar 1 for new flows; rescreening on track for Apr 30", "Financial Crime Ops"],
            ["Compliance Handbook v8", "Distributed Jan 1, training complete Mar 15", "Chief Compliance Officer"],
            ["BSA Officer designation", "Filed Jan 15, 2026", "Office of the General Counsel"],
        ],
    )

    # 3. Training reminders
    _set_heading(doc, "3. Training Reminders", level=1)
    doc.add_paragraph(
        "The Q1 mandatory training topic was Enhanced Due Diligence (EDD). All branch staff are "
        "reminded that high-risk Customers require a 6-month review cycle, source-of-funds narrative, "
        "and ownership tree where applicable. Outstanding training completions are due by April 30, "
        "2026; managers shall escalate non-completion to Regional HR Compliance."
    )
    doc.add_paragraph(
        "Q2 2026 training will focus on Suspicious Activity Reporting (SAR), reaffirming the 30 / 60-"
        "day filing windows and the BSA Officer sign-off requirement before submission."
    )

    # 4. Q2 priorities
    _set_heading(doc, "4. Q2 2026 Priorities", level=1)
    for bullet in [
        "Complete the existing-customer sanctions rescreening (cutover by April 30, 2026).",
        "Roll out SAR mandatory training; target 100% completion by June 15, 2026.",
        "Conduct the semi-annual Exception Log review with the Credit Committee.",
        "Refresh the Customer Complaint Handling Policy following the new CFPB guidance expected in May.",
        "Update the Loan Approval Thresholds wiki page if Q2 portfolio review prompts tier adjustments.",
    ]:
        doc.add_paragraph(bullet, style="List Bullet")

    doc.add_paragraph(
        "Questions or feedback on this update should be directed to the Office of the Chief Compliance "
        "Officer. The next update will be issued by June 30, 2026."
    )

    _footer_para(
        doc,
        "Northvale Demo Bank is fictional. This document exists solely for the GenAI RAG capstone demonstration.",
    )

    out = ATTACH / "quarterly-compliance-update-q1-2026.docx"
    doc.save(out)
    print(f"  wrote {out.relative_to(ATTACH.parent)}")


def main():
    print("Generating DOCX files...")
    credit_officer_decision_framework()
    quarterly_compliance_update()
    print("Done.")


if __name__ == "__main__":
    main()
