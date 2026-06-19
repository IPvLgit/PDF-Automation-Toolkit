"""
PDF Automation Toolkit

A collection of Python tools for PDF workflow automation.

Created by ipvl
"""


#import pip modules

from pypdf import PdfReader, PdfWriter
import os
import sys

#defining the variables as sys arguments

if len(sys.argv) != 3:
    print("Please enter: python(os equivalent) PDF_Merger.py input_folder output_file.pdf")
    sys.exit(1)


input_folder = sys.argv[1]
output_file = sys.argv[2]


writer = PdfWriter()


# Sort files so the order is predictable
pdf_files = sorted(
    f for f in os.listdir(input_folder)
    if f.lower().endswith(".pdf")
)

#validate for no pdfs found

if not pdf_files:
    print("No PDFs found in folder")
    sys.exit(1)

#core for loop

for filename in pdf_files:

    filepath = os.path.join(input_folder, filename)

    reader = PdfReader(filepath)

    for page in reader.pages:
        writer.add_page(page)


with open(output_file, "wb") as file:
    writer.write(file)


print(f"Merged {len(pdf_files)} PDFs into {output_file}") #conforming script ran successfully
