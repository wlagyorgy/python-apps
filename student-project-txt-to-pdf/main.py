import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import pandas as pd

# Create a list of filepaths
filepaths = glob.glob("text-files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    # Add a page to the PDF docs for each text files
    pdf.add_page()

    # Extract the name of the files
    filename = Path(filepath).stem
    print(filename)
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=10, txt=f"{filename.capitalize()}", ln=1)
    with open(f"text-files/{filename}.txt", "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)


# Create the PDF
pdf.output(f"PDFs/animals.pdf")
