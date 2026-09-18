import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)


def create_pdf(filename, title, content):

    folder = os.path.dirname(filename)

    if folder:
        os.makedirs(folder, exist_ok=True)

    document = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#1e3a8a"),
        spaceAfter=15
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#1e3a8a"),
        spaceBefore=10,
        spaceAfter=6
    )

    normal_style = ParagraphStyle(
        "NormalCustom",
        parent=styles["Normal"],
        fontSize=10,
        leading=15,
        spaceAfter=5
    )

    story = []

    story.append(Paragraph(title, title_style))
    story.append(HRFlowable(
        width="100%",
        thickness=1,
        color=colors.HexColor("#2563eb")
    ))
    story.append(Spacer(1, 15))

    lines = content.split("\n")

    headings = [
        "PROFESSIONAL SUMMARY",
        "EDUCATION",
        "TECHNICAL SKILLS",
        "PROJECTS",
        "EXPERIENCE",
        "CAREER OBJECTIVE",
        "DECLARATION",
        "CAREER ROADMAP",
        "TARGET ROLE",
        "LEARNING ROADMAP",
        "PROJECT PHASE",
        "JOB PREPARATION"
    ]

    for line in lines:

        line = line.strip()

        if not line:
            story.append(Spacer(1, 5))
            continue

        safe_line = (
            line.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
        )

        if line in headings:
            story.append(
                Paragraph(safe_line, heading_style)
            )
        elif line.isupper() and len(line) < 40:
            story.append(
                Paragraph(safe_line, heading_style)
            )
        else:
            story.append(
                Paragraph(safe_line, normal_style)
            )

    document.build(story)

    return filename
