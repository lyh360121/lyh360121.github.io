"""Shared font family for the academic CV and industry resume."""
from pathlib import Path

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def register_document_fonts():
    font_dir = Path("C:/Windows/Fonts")
    files = {
        "DocumentSans": "arial.ttf",
        "DocumentSansBold": "arialbd.ttf",
        "DocumentSansItalic": "ariali.ttf",
        "DocumentSansBoldItalic": "arialbi.ttf",
    }
    if all((font_dir / filename).exists() for filename in files.values()):
        for name, filename in files.items():
            pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
        normal, bold, italic, bold_italic = files
    else:
        normal, bold, italic, bold_italic = (
            "Helvetica", "Helvetica-Bold", "Helvetica-Oblique", "Helvetica-BoldOblique"
        )
    pdfmetrics.registerFontFamily(
        normal, normal=normal, bold=bold, italic=italic, boldItalic=bold_italic
    )
    return normal, bold, italic, bold_italic
