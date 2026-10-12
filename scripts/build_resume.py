"""Generate the one-page industry resume; academic CV uses build_cv.py.

Usage: python scripts/build_resume.py --output static/uploads/Yonghui_Liu_Resume.pdf
Dependencies: reportlab, PyYAML. Optional --phone creates a private application copy.
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
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, default=ROOT / 'output/pdf/Yonghui_Liu_Resume.pdf')
parser.add_argument('--phone', default='')
args = parser.parse_args()
out = args.output.resolve()
out.parent.mkdir(parents=True, exist_ok=True)
author = yaml.safe_load((ROOT / 'data/authors/me.yaml').read_text(encoding='utf-8'))
content = yaml.safe_load((ROOT / 'data/resume.yaml').read_text(encoding='utf-8'))['industry']

font_dir = Path('C:/Windows/Fonts')
if (font_dir / 'arial.ttf').exists() and (font_dir / 'arialbd.ttf').exists():
    pdfmetrics.registerFont(TTFont('ResumeSans', str(font_dir / 'arial.ttf')))
    pdfmetrics.registerFont(TTFont('ResumeSansBold', str(font_dir / 'arialbd.ttf')))
    normal, bold = 'ResumeSans', 'ResumeSansBold'
    pdfmetrics.registerFontFamily(normal, normal=normal, bold=bold)
else:
    normal, bold = 'Helvetica', 'Helvetica-Bold'

INK = colors.HexColor('#181818')
GRAY = colors.HexColor('#454545')
WIDTH = A4[0] - 112
styles = {
    'name': ParagraphStyle('name', fontName=bold, fontSize=24, leading=29,
        textColor=INK, spaceAfter=3),
    'headline': ParagraphStyle('headline', fontName=normal, fontSize=11.5, leading=15,
        textColor=INK, spaceAfter=4),
    'contact': ParagraphStyle('contact', fontName=normal, fontSize=10.3, leading=14,
        textColor=INK, spaceAfter=4),
    'section': ParagraphStyle('section', fontName=bold, fontSize=12.5, leading=16,
        textColor=INK, spaceBefore=13, spaceAfter=4, keepWithNext=True),
    'entry': ParagraphStyle('entry', fontName=bold, fontSize=11.1, leading=14.6,
        textColor=INK, spaceAfter=3, keepWithNext=True),
    'date': ParagraphStyle('date', fontName=normal, fontSize=10.5, leading=14.6,
        textColor=GRAY, alignment=TA_RIGHT),
    'body': ParagraphStyle('body', fontName=normal, fontSize=11, leading=14.8,
        textColor=INK, spaceAfter=3),
    'bullet': ParagraphStyle('bullet', fontName=normal, fontSize=11, leading=14.8,
        textColor=INK, leftIndent=11, firstLineIndent=-10, spaceAfter=4),
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
    story.extend([
        p(label.upper(), 'section'),
        HRFlowable(width='100%', thickness=.55, color=colors.HexColor('#b7b7b7'), spaceAfter=6),
    ])

name = author['name']['display']
email_url = next(entry['url'] for entry in author['links'] if entry['url'].startswith('mailto:'))
github = next(entry['url'] for entry in author['links'] if entry['url'].startswith('https://github.com/'))
contacts = [
    f'<link href="{escape(email_url)}">{text(email_url.removeprefix("mailto:"))}</link>',
    '<link href="https://lyh360121.github.io/">lyh360121.github.io</link>',
    f'<link href="{escape(github)}">GitHub</link>',
]
if args.phone:
    contacts.append(text(args.phone))
story.extend([
    p(text(name), 'name'),
    p(text(content['headline']), 'headline'),
    p(' &nbsp;|&nbsp; '.join(contacts), 'contact'),
])

section('Technical Skills')
for entry in content['skills']:
    story.append(p(f'<b>{text(entry["label"])}:</b> {text(entry["text"])}'))

section('Experience')
research = content['research']
pieces = [row(text(research['title']), date_range(author['education'][0]))]
pieces.extend(p('- ' + text(bullet), 'bullet') for bullet in research['bullets'])
story.extend([KeepTogether(pieces), Spacer(1, 7)])
for entry in author['experience']:
    if entry['org'] == 'Meituan':
        pieces = [row(f'{text(entry["role"])} | {text(entry["org"])}', date_range(entry))]
    else:
        pieces = [row(text(entry['role']), date_range(entry)), p(text(entry['org']))]
    story.extend([KeepTogether(pieces), Spacer(1, 5)])

section('Projects')
for project in content['projects']:
    title = f'<link href="https://lyh360121.github.io{project["url"]}">{text(project["title"])}</link>'
    story.extend([
        KeepTogether([row(title, text(project['status'])), p('- ' + text(project['text']), 'bullet')]),
        Spacer(1, 5),
    ])

section('Education')
degrees = {'PhD': 'Ph.D. candidate', 'MS': 'M.S. in Ocean Engineering', 'BS': 'B.S. in Physics'}
for entry in author['education']:
    institution = 'KAIST' if entry['degree'] == 'PhD' else entry['institution'].split(' (')[0]
    pieces = [row(f'{text(institution)} | {text(degrees[entry["degree"]])}', date_range(entry))]
    if entry['degree'] == 'PhD':
        pieces.append(p('Cho Chun Shik Graduate School of Mobility'))
    story.extend([KeepTogether(pieces), Spacer(1, 3)])

section('Publications')
story.append(p(f'<link href="https://lyh360121.github.io/publications/">{text(content["publication_record"])}</link>'))

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
