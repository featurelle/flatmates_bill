import webbrowser
from pathlib import Path

from billing.billing import Bill, Flatmate
from billing.reports import generate

PDF_PATH = str(Path.cwd() / 'files' / 'report.pdf')

flatmate1 = Flatmate('John', 22)
flatmate2 = Flatmate('Jimmy', 27)

bill = Bill(1555, 'April 2021')

generate(PDF_PATH, Flatmate.calc_shares(bill))
webbrowser.open(PDF_PATH)
