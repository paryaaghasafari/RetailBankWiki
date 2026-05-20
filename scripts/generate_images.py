"""Generate the 4 flowchart PNGs for the Northvale Demo Bank wiki.

Outputs to attachments/:
  - onboarding-flow.png
  - credit-decision-tree.png
  - sanctions-screening-flow.png
  - aml-escalation-process.png

All diagrams are fictional and for demonstration only.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "attachments"
OUT_DIR.mkdir(parents=True, exist_ok=True)

NAVY = "#1a237e"
INDIGO = "#3949ab"
TEAL = "#00897b"
AMBER = "#ef6c00"
RED = "#c62828"
GREY = "#546e7a"
LIGHT = "#eceff1"
WHITE = "#ffffff"


def _new_canvas(width_in: float = 12.0, height_in: float = 8.0):
    fig, ax = plt.subplots(figsize=(width_in, height_in), dpi=150)
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 80)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.patch.set_facecolor(WHITE)
    return fig, ax


def _box(ax, x, y, w, h, text, fill=INDIGO, edge=NAVY, text_color=WHITE, fontsize=10, bold=True):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.4,rounding_size=1.2",
        linewidth=1.6,
        edgecolor=edge,
        facecolor=fill,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        color=text_color,
        fontsize=fontsize,
        fontweight="bold" if bold else "normal",
        wrap=True,
    )


def _diamond(ax, cx, cy, w, h, text, fill=AMBER, edge=NAVY, fontsize=9):
    pts = [[cx, cy + h / 2], [cx + w / 2, cy], [cx, cy - h / 2], [cx - w / 2, cy]]
    poly = plt.Polygon(pts, closed=True, facecolor=fill, edgecolor=edge, linewidth=1.6)
    ax.add_patch(poly)
    ax.text(cx, cy, text, ha="center", va="center", color=WHITE, fontsize=fontsize, fontweight="bold")
    return {
        "top": (cx, cy + h / 2),
        "right": (cx + w / 2, cy),
        "bottom": (cx, cy - h / 2),
        "left": (cx - w / 2, cy),
        "center": (cx, cy),
    }


def _arrow(ax, p1, p2, label: str | None = None, label_offset=(0.0, 0.0), color=GREY):
    arr = FancyArrowPatch(
        p1,
        p2,
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=1.6,
        color=color,
    )
    ax.add_patch(arr)
    if label:
        mx, my = (p1[0] + p2[0]) / 2 + label_offset[0], (p1[1] + p2[1]) / 2 + label_offset[1]
        ax.text(
            mx,
            my,
            label,
            color=NAVY,
            fontsize=9,
            fontweight="bold",
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.25", facecolor=WHITE, edgecolor="none"),
        )


def _title(ax, text: str, subtitle: str | None = None):
    ax.text(
        60,
        76.5,
        text,
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color=NAVY,
    )
    if subtitle:
        ax.text(
            60,
            73,
            subtitle,
            ha="center",
            va="center",
            fontsize=9,
            color=GREY,
            style="italic",
        )


def _footer(ax, text="Northvale Demo Bank - FICTIONAL FOR DEMONSTRATION"):
    ax.text(60, 1.5, text, ha="center", va="center", fontsize=8, color=GREY, style="italic")


def _save(fig, name: str):
    out = OUT_DIR / name
    fig.savefig(out, dpi=150, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"  wrote {out.relative_to(OUT_DIR.parent)}")


# ---------------------------------------------------------------------------
# 1. Onboarding flow (KYC)
# ---------------------------------------------------------------------------
def onboarding_flow():
    fig, ax = _new_canvas()
    _title(ax, "Customer Onboarding Flow", "KYC / CIP - target completion within 30 calendar days")

    # Row 1: four blue gates left-to-right
    _box(ax, 2, 60, 22, 8, "Application\nReceived", fill=INDIGO)
    _box(ax, 30, 60, 22, 8, "Identity Verification\n(CIP)", fill=INDIGO)
    _box(ax, 58, 60, 22, 8, "Sanctions / PEP\nScreening", fill=INDIGO)
    _box(ax, 86, 60, 32, 8, "Customer Due Diligence\n(CDD Risk Rating)", fill=INDIGO)

    _arrow(ax, (24, 64), (30, 64))
    _arrow(ax, (52, 64), (58, 64))
    _arrow(ax, (80, 64), (86, 64))

    # Centered High-Risk diamond
    d = _diamond(ax, 60, 44, 22, 12, "High Risk?", fill=AMBER, fontsize=10)

    # Single connector from CDD box down/left to top of diamond
    _arrow(ax, (102, 60), (60, 50))

    # EDD (left) and Standard (right) tier
    _box(ax, 6, 26, 36, 12, "Enhanced Due Diligence\n(EDD) + Senior Approval", fill=TEAL)
    _box(ax, 78, 26, 36, 12, "Standard Approval\nWorkflow", fill=TEAL)

    _arrow(ax, d["left"], (24, 32), label="Yes", label_offset=(-1, 3))
    _arrow(ax, d["right"], (96, 32), label="No", label_offset=(1, 3))

    # Bottom navy result boxes
    _box(ax, 22, 6, 32, 10, "Account Opened\n+ Welcome Pack", fill=NAVY)
    _box(ax, 66, 6, 32, 10, "Ongoing Monitoring\nScheduled", fill=NAVY)

    _arrow(ax, (24, 26), (38, 16))                                       # EDD -> Account Opened
    _arrow(ax, (96, 26), (82, 16))                                       # Standard -> Ongoing Monitoring
    _arrow(ax, (54, 11), (66, 11))                                       # Account Opened -> Ongoing

    _footer(ax)
    _save(fig, "onboarding-flow.png")


# ---------------------------------------------------------------------------
# 2. Credit decision tree
# ---------------------------------------------------------------------------
def credit_decision_tree():
    fig, ax = _new_canvas()
    _title(ax, "Credit Decision Tree", "Unsecured personal loans - tiered approval authority")

    # Top: Loan application box
    _box(ax, 50, 64, 20, 8, "Loan Application", fill=INDIGO)

    # FICO / DTI gate diamond
    gate = _diamond(ax, 60, 52, 24, 10, "FICO >= 660\nDTI <= 36%?", fill=AMBER, fontsize=9)
    _arrow(ax, (60, 64), (60, 57))

    # Decline path
    _box(ax, 6, 48, 26, 8, "Decline or Refer to\nSecured Product", fill=RED)
    _arrow(ax, gate["left"], (32, 52), label="No", label_offset=(-2, 2.5))

    # Amount diamond 1: <= $25k -> T1
    d25 = _diamond(ax, 90, 52, 22, 10, "Amount\n<= $25,000?", fill=AMBER, fontsize=9)
    _arrow(ax, gate["right"], d25["left"], label="Yes", label_offset=(0, 2.5))

    _box(ax, 100, 32, 18, 8, "Tier 1:\nBranch Manager", fill=TEAL, fontsize=9)
    _arrow(ax, d25["bottom"], (109, 40), label="Yes", label_offset=(3, 2))

    # Amount diamond 2: <= $100k -> T2
    d100 = _diamond(ax, 60, 32, 22, 10, "Amount\n<= $100,000?", fill=AMBER, fontsize=9)
    _arrow(ax, d25["left"], d100["right"], label="No", label_offset=(0, 2.5))

    _box(ax, 50, 14, 20, 8, "Tier 2:\nRegional CO", fill=TEAL, fontsize=9)
    _arrow(ax, d100["bottom"], (60, 22), label="Yes", label_offset=(3, 2))

    # Amount diamond 3: <= $500k -> T3
    d500 = _diamond(ax, 30, 32, 22, 10, "Amount\n<= $500,000?", fill=AMBER, fontsize=9)
    _arrow(ax, d100["left"], d500["right"], label="No", label_offset=(0, 2.5))

    _box(ax, 22, 14, 16, 8, "Tier 3:\nCredit Cmte", fill=TEAL, fontsize=9)
    _arrow(ax, d500["bottom"], (30, 22), label="Yes", label_offset=(3, 2))

    # T4 (no path) — place below Tier 3 so the "No" label has room
    _box(ax, 2, 14, 18, 8, "Tier 4:\nBoard Cmte", fill=NAVY, fontsize=9)
    _arrow(ax, d500["left"], (11, 22), label="No", label_offset=(-3, 3))

    _footer(ax)
    _save(fig, "credit-decision-tree.png")


# ---------------------------------------------------------------------------
# 3. Sanctions screening flow (already clean — keep)
# ---------------------------------------------------------------------------
def sanctions_screening_flow():
    fig, ax = _new_canvas()
    _title(ax, "Sanctions Screening Flow", "OFAC SDN + UN + EU lists - daily refresh, 4-hour match-review SLA")

    _box(ax, 2, 60, 22, 10, "Inbound Name\n(onboarding /\ntransaction)", fill=INDIGO, fontsize=8)
    _box(ax, 30, 60, 22, 10, "Normalize +\nTransliterate", fill=INDIGO, fontsize=9)
    _box(ax, 58, 60, 22, 10, "Fuzzy Match\nvs Watchlists", fill=INDIGO, fontsize=9)
    sim = _diamond(ax, 100, 65, 28, 12, "Similarity\n>= 85%?", fill=AMBER, fontsize=9)

    _arrow(ax, (24, 65), (30, 65))
    _arrow(ax, (52, 65), (58, 65))
    _arrow(ax, (80, 65), sim["left"])

    _box(ax, 88, 38, 24, 10, "Auto-Clear +\nLog Hit", fill=TEAL)
    _arrow(ax, sim["bottom"], (100, 48), label="No", label_offset=(4, 4))

    _box(ax, 52, 38, 30, 10, "Generate Alert\n(Tier 1 Analyst)", fill=AMBER)
    _arrow(ax, sim["left"], (82, 43), label="Yes", label_offset=(-3, 3))

    tm = _diamond(ax, 67, 18, 30, 12, "True Match?\n(4-hr SLA)", fill=AMBER, fontsize=9)
    _arrow(ax, (67, 38), (67, 24))

    _box(ax, 4, 14, 38, 12, "Block Transaction\n+ Freeze Funds\n+ File OFAC Report (10 days)", fill=RED, fontsize=8.5)
    _arrow(ax, tm["left"], (42, 18), label="Yes", label_offset=(0, 2.5))

    _box(ax, 92, 14, 26, 12, "Release +\nDocument\nFalse Positive", fill=TEAL, fontsize=9)
    _arrow(ax, tm["right"], (92, 18), label="No", label_offset=(0, 2.5))

    _footer(ax)
    _save(fig, "sanctions-screening-flow.png")


# ---------------------------------------------------------------------------
# 4. AML escalation process
# ---------------------------------------------------------------------------
def aml_escalation_process():
    fig, ax = _new_canvas()
    _title(ax, "AML Escalation Process", "Transaction monitoring -> investigation -> SAR filing within 30 days")

    # Row 1
    _box(ax, 2, 62, 26, 8, "Transaction\nMonitoring Alert", fill=INDIGO)
    _box(ax, 34, 62, 26, 8, "L1 Analyst Triage\n(2 business days)", fill=INDIGO)
    rs = _diamond(ax, 78, 66, 22, 12, "Reasonable\nSuspicion?", fill=AMBER)

    _arrow(ax, (28, 66), (34, 66))
    _arrow(ax, (60, 66), rs["left"])

    _box(ax, 98, 62, 20, 8, "Close +\nDocument", fill=TEAL, fontsize=9)
    _arrow(ax, rs["right"], (98, 66), label="No", label_offset=(0, 2.5))

    # Row 2: L2 Investigator
    _box(ax, 66, 42, 26, 10, "L2 Investigator\n(10 business days)", fill=INDIGO, fontsize=9)
    _arrow(ax, rs["bottom"], (79, 52), label="Yes", label_offset=(3, 2))

    # File SAR? diamond
    sar = _diamond(ax, 79, 28, 22, 10, "File SAR?", fill=AMBER)
    _arrow(ax, (79, 42), (79, 33))

    # Enhanced Monitoring on left (No branch)
    _box(ax, 38, 24, 24, 8, "Enhanced\nMonitoring (180 days)", fill=TEAL, fontsize=8.5)
    _arrow(ax, sar["left"], (62, 28), label="No", label_offset=(0, 2.5))

    # BSA Officer review + sign-off (Yes branch -> down)
    _box(ax, 66, 10, 26, 8, "BSA Officer\nReview + Sign-off", fill=NAVY, fontsize=9)
    _arrow(ax, sar["bottom"], (79, 18), label="Yes", label_offset=(3, 2))

    # File FinCEN SAR
    _box(ax, 38, 10, 24, 8, "File FinCEN SAR\n(30 / 60 days)", fill=RED, fontsize=9)
    _arrow(ax, (66, 14), (62, 14))

    # CTR Filing as parallel red box at top-right
    _box(ax, 98, 24, 20, 12, "CTR Filing if\nCash > $10,000\n(15 days)", fill=RED, fontsize=8)

    _footer(ax)
    _save(fig, "aml-escalation-process.png")


def main():
    print("Generating PNG flowcharts...")
    onboarding_flow()
    credit_decision_tree()
    sanctions_screening_flow()
    aml_escalation_process()
    print("Done.")


if __name__ == "__main__":
    main()
