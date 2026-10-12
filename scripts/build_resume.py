"""Generate the one-page industry resume; academic CV uses build_cv.py.

Usage: python scripts/build_resume.py --phone YOUR_PHONE
Dependencies: reportlab, PyYAML. The resume is a local application document.
"""
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import (
    Flowable, HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

from pdf_style import register_document_fonts

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, default=ROOT / 'output/pdf/Yonghui_Liu_Resume.pdf')
parser.add_argument('--phone', default='')
parser.add_argument('--photo', type=Path, default=ROOT / 'assets/media/authors/me.jpg')
args = parser.parse_args()
out = args.output.resolve()
out.parent.mkdir(parents=True, exist_ok=True)
author = yaml.safe_load((ROOT / 'data/authors/me.yaml').read_text(encoding='utf-8'))
resume_data = yaml.safe_load((ROOT / 'data/resume.yaml').read_text(encoding='utf-8'))
content = resume_data['industry']
normal, bold, italic, bold_italic = register_document_fonts()

INK = colors.HexColor('#202932')
ACCENT = colors.HexColor('#18344d')
GRAY = colors.HexColor('#454545')
WIDTH = A4[0] - 112
styles = {
    'name': ParagraphStyle('name', fontName=bold, fontSize=24, leading=29,
        textColor=ACCENT, spaceAfter=5),
    'headline': ParagraphStyle('headline', fontName=normal, fontSize=11, leading=14.1,
        textColor=INK, spaceAfter=4),
    'role': ParagraphStyle('role', fontName=normal, fontSize=10.5, leading=13.4,
        textColor=GRAY, spaceAfter=7),
    'contact': ParagraphStyle('contact', fontName=normal, fontSize=10.5, leading=13.4,
        textColor=INK, spaceAfter=2),
    'section': ParagraphStyle('section', fontName=bold, fontSize=12.5, leading=16,
        textColor=ACCENT, spaceBefore=8, spaceAfter=3, keepWithNext=True),
    'entry': ParagraphStyle('entry', fontName=bold, fontSize=11, leading=14.1,
        textColor=INK, spaceAfter=3, keepWithNext=True),
    'date': ParagraphStyle('date', fontName=normal, fontSize=10.5, leading=14.1,
        textColor=GRAY, alignment=TA_RIGHT),
    'body': ParagraphStyle('body', fontName=normal, fontSize=11, leading=14.1,
        textColor=INK, spaceAfter=2),
    'bullet': ParagraphStyle('bullet', fontName=normal, fontSize=11, leading=14.1,
        textColor=INK, leftIndent=11, firstLineIndent=-10, spaceAfter=3),
    'publication': ParagraphStyle('publication', fontName=normal, fontSize=11, leading=14.1,
        textColor=INK, leftIndent=13, firstLineIndent=-13, spaceAfter=3),
}

def text(value):
    return escape(str(value).replace('\u2013', '-').replace('\u2014', '-'))

def p(value, style='body'):
    return Paragraph(value, styles[style])

def date_range(entry):
    start = datetime.fromisoformat(entry['start']).strftime('%b %Y')
    end = datetime.fromisoformat(entry['end']).strftime('%b %Y') if entry.get('end') else 'Present'
    return text(f'{start} - {end}')

def row(left, right):
    table = Table([[p(left, 'entry'), p(right, 'date')]],
        colWidths=[WIDTH - 136, 136], hAlign='LEFT')
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    return table

story = []
def section(label):
    rule = HRFlowable(width='100%', thickness=.55, color=colors.HexColor('#b7c2cb'), spaceAfter=4)
    rule.keepWithNext = True
    story.extend([
        p(label, 'section'),
        rule,
    ])

class Portrait(Flowable):
    """Place the existing photograph in a head-and-shoulders frame, without changing it."""
    def __init__(self, path, width=82, height=106):
        super().__init__()
        self.width, self.height = width, height
        self.image = ImageReader(str(path))
        self.source_width, self.source_height = self.image.getSize()

    def draw(self):
        canvas = self.canv
        # Normalized head-and-shoulders window in the original website photograph.
        left, top, crop_width, crop_height = .50, .31, .32, .32
        crop_width *= self.source_width
        crop_height *= self.source_height
        scale = max(self.width / crop_width, self.height / crop_height)
        x = -left * self.source_width * scale + (self.width - crop_width * scale) / 2
        y = -(self.source_height * (1 - top) - crop_height) * scale
        y += (self.height - crop_height * scale) / 2
        canvas.saveState()
        path = canvas.beginPath()
        path.roundRect(0, 0, self.width, self.height, 2)
        canvas.clipPath(path, stroke=0, fill=0)
        canvas.drawImage(self.image, x, y, width=self.source_width * scale,
            height=self.source_height * scale, mask='auto')
        canvas.restoreState()
        canvas.setStrokeColor(colors.HexColor('#c6cdd3'))
        canvas.setLineWidth(.45)
        canvas.roundRect(0, 0, self.width, self.height, 2, stroke=1, fill=0)

name = author['name']['display']
email_url = next(entry['url'] for entry in author['links'] if entry['url'].startswith('mailto:'))
github = next(entry['url'] for entry in author['links'] if entry['url'].startswith('https://github.com/'))
contacts = [f'<link href="{escape(email_url)}">{text(email_url.removeprefix("mailto:"))}</link>']
if args.phone:
    contacts.append(text(args.phone))
header_text = [
    p(text(name), 'name'),
    p(text(content['headline']), 'headline'),
    p('Ph.D. Candidate, KAIST', 'role'),
    p(' &nbsp;|&nbsp; '.join(contacts), 'contact'),
    p('<link href="https://lyh360121.github.io/">lyh360121.github.io</link>'
      f' &nbsp;|&nbsp; <link href="{escape(github)}">GitHub</link>', 'contact'),
]
header = Table([[header_text, Portrait(args.photo.resolve())]],
    colWidths=[WIDTH - 106, 106], hAlign='LEFT')
header.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
    ('LEFTPADDING', (0, 0), (-1, -1), 0),
    ('RIGHTPADDING', (0, 0), (0, 0), 14),
    ('RIGHTPADDING', (1, 0), (1, 0), 0),
    ('TOPPADDING', (0, 0), (-1, -1), 0),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
]))
story.extend([header, Spacer(1, 7),
    HRFlowable(width='100%', thickness=1.1, color=ACCENT, spaceAfter=2)])

section('Education')
degrees = {'PhD': 'Ph.D. candidate', 'MS': 'M.S. in Ocean Engineering', 'BS': 'B.S. in Physics'}
for entry in author['education']:
    institution = 'KAIST' if entry['degree'] == 'PhD' else entry['institution'].split(' (')[0]
    pieces = [row(f'{text(institution)} | {text(degrees[entry["degree"]])}', date_range(entry))]
    story.extend([KeepTogether(pieces), Spacer(1, 2)])

section('Experience')
research = content['research']
pieces = [row(text(research['title']), date_range(author['education'][0]))]
pieces.extend(p('- ' + text(bullet), 'bullet') for bullet in research['bullets'])
story.extend([KeepTogether(pieces), Spacer(1, 3)])
for entry in author['experience']:
    if entry['org'] == 'Meituan':
        pieces = [row(f'{text(entry["role"])} | {text(entry["org"])}', date_range(entry))]
    else:
        pieces = [row(text(entry['role']), date_range(entry)), p(text(entry['org']))]
    story.extend([KeepTogether(pieces), Spacer(1, 3)])

section('Projects')
for project in content['projects']:
    title = f'<link href="https://lyh360121.github.io{project["url"]}">{text(project["title"])}</link>'
    story.extend([
        KeepTogether([row(title, text(project['status'])), p('- ' + text(project['text']), 'bullet')]),
        Spacer(1, 3),
    ])

section('Technical Skills')
for entry in content['skills']:
    story.append(p(f'<b>{text(entry["label"])}:</b> {text(entry["text"])}'))

section('Selected Publications (First Author)')
venue_names = {
    'Knowledge-Based Systems': 'Knowledge-Based Systems (KBS)',
    'Communications in Transportation Research': 'Communications in Transportation Research (COMMTR)',
    '2025 IEEE 28th International Conference on Intelligent Transportation Systems (ITSC)': 'IEEE ITSC',
}
for number, reference in enumerate(content['publication_refs'], 1):
    paper = resume_data['cv_publications'][reference - 1]
    if paper['authors'][0] != name:
        raise ValueError('Selected publication must be first-authored by the resume owner.')
    title = f'<link href="https://doi.org/{escape(paper["doi"])}">{text(paper["title"])}</link>'
    venue = venue_names.get(paper['venue'], paper['venue'])
    story.append(KeepTogether([
        p(f'{number}. {title}<br/><i>{text(venue)}</i>, {paper["year"]}.', 'publication')
    ]))

pending = out.with_suffix('.building.pdf')
doc = SimpleDocTemplate(str(pending), pagesize=A4, leftMargin=50, rightMargin=50,
    topMargin=42, bottomMargin=42, title=f'{name} - Resume', author=name,
    subject='Industry resume: machine learning research and software engineering')
doc.build(story)
if doc.page != 1:
    pending.unlink()
    raise ValueError(f'Resume must fit one readable page; generated {doc.page}. Edit content instead of shrinking the font.')
pending.replace(out)
print(out)
