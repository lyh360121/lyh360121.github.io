"""Generate the two-page academic CV from versioned research and author data.

Usage: python scripts/build_cv.py --output static/uploads/Yonghui_Liu_CV.pdf
Default output: output/pdf/Yonghui_Liu_Academic_CV.pdf
Dependencies: reportlab, PyYAML.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate,
    Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--output", type=Path, default=ROOT / "output/pdf/Yonghui_Liu_Academic_CV.pdf")
args = parser.parse_args()
out = args.output.resolve()
out.parent.mkdir(parents=True, exist_ok=True)
resume = yaml.safe_load((ROOT / "data/resume.yaml").read_text(encoding="utf-8"))
author = yaml.safe_load((ROOT / "data/authors/me.yaml").read_text(encoding="utf-8"))

font_dir = Path("C:/Windows/Fonts")
font_files = {"CVSerif": "times.ttf", "CVSerifBold": "timesbd.ttf", "CVSerifItalic": "timesi.ttf"}
if all((font_dir / f).exists() for f in font_files.values()):
    for name, filename in font_files.items():
        pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
    normal, bold, italic = "CVSerif", "CVSerifBold", "CVSerifItalic"
    pdfmetrics.registerFontFamily(normal, normal=normal, bold=bold, italic=italic, boldItalic=bold)
else:
    normal, bold, italic = "Times-Roman", "Times-Bold", "Times-Italic"

INK = colors.HexColor("#161616")
GRAY = colors.HexColor("#555555")
RULE = colors.HexColor("#b6b6b6")
WIDTH = A4[0] - 112  # Document margins plus Platypus frame padding.
base = dict(fontName=normal, fontSize=11, leading=14.1, textColor=INK)
styles = {
    "body": ParagraphStyle("body", **base),
    "name": ParagraphStyle("name", fontName=bold, fontSize=22, leading=26,
        textColor=INK, alignment=TA_CENTER, spaceAfter=3),
    "role": ParagraphStyle("role", **base, alignment=TA_CENTER, spaceAfter=3),
    "contact": ParagraphStyle("contact", fontName=normal, fontSize=10.5, leading=13.4,
        textColor=INK, alignment=TA_CENTER, spaceAfter=7),
    "topic": ParagraphStyle("topic", fontName=bold, fontSize=11, leading=14.1,
        textColor=INK, spaceBefore=3, spaceAfter=3, keepWithNext=True),
    "section": ParagraphStyle("section", fontName=bold, fontSize=13.3, leading=16,
        textColor=INK, spaceBefore=9, spaceAfter=3, keepWithNext=True),
    "entry": ParagraphStyle("entry", fontName=bold, fontSize=11.5, leading=14.3,
        textColor=INK, spaceAfter=3, keepWithNext=True),
    "date": ParagraphStyle("date", fontName=normal, fontSize=10.5, leading=14.3,
        textColor=INK, alignment=TA_RIGHT),
    "status": ParagraphStyle("status", fontName=italic, fontSize=10.2, leading=13.4,
        textColor=GRAY, alignment=TA_RIGHT),
    "detail": ParagraphStyle("detail", **base, spaceAfter=3),
    "bullet": ParagraphStyle("bullet", **base, leftIndent=11, firstLineIndent=-9,
        spaceAfter=3.4),
    "citation": ParagraphStyle("citation", fontName=normal, fontSize=11, leading=14.4,
        textColor=INK, leftIndent=16, firstLineIndent=-16, spaceAfter=8),
}

def text(value):
    return escape(str(value).replace("\u2013", "-").replace("\u2014", "-"))

def p(value, style="body"):
    return Paragraph(value, styles[style])

story = []
def section(label):
    story.extend([
        p(text(label), "section"),
        HRFlowable(width="100%", thickness=.5, color=RULE, spaceAfter=5),
    ])

def row(left, right, right_style="date"):
    result = Table([[p(left, "entry"), p(right, right_style)]],
        colWidths=[WIDTH-120, 120], hAlign="LEFT")
    result.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    return result

def date_range(record):
    from datetime import datetime
    start = datetime.fromisoformat(record["start"]).strftime("%b %Y")
    end = datetime.fromisoformat(record["end"]).strftime("%b %Y") if record.get("end") else "Present"
    return text(f"{start} - {end}")

name = author["name"]["display"]
email_url = next(link["url"] for link in author["links"] if link["url"].startswith("mailto:"))
email = email_url.removeprefix("mailto:")
contact = [f'<link href="{escape(email_url)}">{text(email)}</link>',
    '<link href="https://lyh360121.github.io/">lyh360121.github.io</link>']
story.extend([
    p(text(name), "name"),
    p("Ph.D. Candidate, KAIST", "role"),
    p(" &nbsp;|&nbsp; ".join(contact), "contact"),
])

thesis_title = "Compression-Reconstruction Co-Design for Urban Mobility Trajectories"
doctoral_record = next(entry for entry in author["education"] if entry["degree"] == "PhD")

section("Education")
degree_names = {"PhD": "Ph.D. candidate", "MS": "M.S.", "BS": "B.S."}
for entry in author["education"]:
    institution = "KAIST" if entry["degree"] == "PhD" else entry["institution"]
    detail = degree_names.get(entry["degree"], entry["degree"])
    if entry.get("summary"):
        detail += ", " + entry["summary"]
    pieces = [row(text(institution), date_range(entry)), p(text(detail), "detail")]
    if entry["degree"] == "PhD":
        pieces.append(p(f'<b>Doctoral thesis:</b> <i>{text(thesis_title)}</i> (in progress).', "detail"))
    story.append(KeepTogether(pieces))
    story.append(Spacer(1, 2))

section("Research Experience")
story.extend([
    row("Doctoral Research, KAIST", date_range(doctoral_record)),
    p("Research on trajectory observation-reconstruction co-design, with published studies "
      "in trajectory modeling and road-network representation learning.", "detail"),
])
papers = resume["cv_publications"]
for research in resume["cv_research"]:
    pieces = [p(text(research["title"]), "topic")]
    for item in research["items"]:
        number = item["reference"]
        doi = papers[number - 1]["doi"]
        pieces.append(p(f'- <b>{text(item["label"])}.</b> {text(item["text"])} '
            f'<link href="https://doi.org/{doi}">[{number}]</link>', "bullet"))
    story.append(KeepTogether(pieces))
    story.append(Spacer(1, 1))

section("Current Research Projects")
for project in resume["projects"]:
    title = f'<link href="https://lyh360121.github.io{project["url"]}">{text(project["title"])}</link>'
    pieces = [row(title, text(project["status"]), "status")]
    pieces.extend(p("- " + text(bullet), "bullet") for bullet in project["bullets"])
    story.append(KeepTogether(pieces))
    story.append(Spacer(1, 2))

story.append(PageBreak())
section("Publications")
for group in ("Journal Articles", "Conference Papers"):
    story.append(p(group, "entry"))
    for index, paper in enumerate(papers, 1):
        if paper["group"] != group:
            continue
        authors = [f"<b>{text(a)}</b>" if a == name else text(a) for a in paper["authors"]]
        author_text = ", ".join(authors[:-1]) + " and " + authors[-1] if len(authors)>1 else authors[0]
        title = f'<link href="https://doi.org/{paper["doi"]}">{text(paper["title"])}</link>'
        citation = f'{index}. {author_text}. {title}. <i>{text(paper["venue"])}</i>, '
        citation += f'{text(paper["detail"])}, {paper["year"]}.'
        story.append(p(citation, "citation"))

section("Professional Experience")
for entry in author["experience"]:
    pieces = [row(text(entry["role"]), date_range(entry)), p(text(entry["org"]), "detail")]
    story.append(KeepTogether(pieces))
    story.append(Spacer(1, 2))

section("Technical Skills")
for skill in resume["skills"]:
    story.append(p(f'<b>{text(skill["label"])}:</b> {text(skill["text"])}', "detail"))
section("Languages")
story.append(p("; ".join(f'<b>{text(entry["name"])}</b>: {text(entry["label"])}'
    for entry in author["languages"])))

def decoration(canvas, doc):
    canvas.setTitle("Yonghui Liu - Academic Curriculum Vitae")
    canvas.setAuthor(name)
    canvas.setSubject("Education, doctoral research, publications, and professional experience")
    canvas.setFillColor(GRAY)
    canvas.setFont(normal, 9)
    canvas.drawString(56, 26, "Yonghui Liu | Curriculum Vitae | October 2026")
    canvas.drawRightString(A4[0]-56, 26, f"{doc.page} / 2")
    if doc.page > 1:
        canvas.setFont(bold, 11)
        canvas.drawString(56, A4[1]-30, name)
        canvas.setFont(normal, 10)
        canvas.drawRightString(A4[0]-56, A4[1]-30, "Academic Curriculum Vitae")

doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=50, rightMargin=50,
    topMargin=39, bottomMargin=41, title="Yonghui Liu - Academic Curriculum Vitae", author=name)
doc.build(story, onFirstPage=decoration, onLaterPages=decoration)
print(out)
