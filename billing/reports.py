from pathlib import Path

from fpdf import FPDF


IMG_PATH = str(Path(__package__).resolve().parent / 'files' / 'img.png')


def _init(period: str) -> FPDF:
    pdf = FPDF(orientation='P', unit='pt', format='A4')

    pdf.add_page()
    pdf.image(IMG_PATH, w=125)
    pdf.set_font(family='Times', size=24, style='B')

    pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)
    pdf.cell(w=150, h=40, txt='Period:', border=1)
    pdf.cell(w=0, h=40, txt=period, border=1, align='R', ln=1)

    pdf.set_font(family='Times', size=18)

    return pdf


def _add_row(pdf: FPDF, share: dict) -> None:
    pdf.cell(w=150, h=40, txt=f'{share["name"]}', border=1)
    pdf.cell(w=0, h=40, txt=f'{round(share["share"], 2)} USD', border=1, align='R', ln=1)


def generate(filename: str, shares_data: dict) -> None:
    pdf = _init(shares_data['period'])
    for share in shares_data['shares']:
        _add_row(pdf, share)
    pdf.output(filename)
