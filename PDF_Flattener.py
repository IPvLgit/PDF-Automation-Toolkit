"""
PDF Automation Toolkit

A collection of Python tools for PDF workflow automation.

Created by ipvl
"""


#import pip modules

from pypdf import PdfReader, PdfWriter
import fitz
import os
import sys

#defining the variables as sys arguments

if len(sys.argv) != 3:
    print("Please enter: python(os equivalent) PDF_Flattener.py input_folder output_folder")
    sys.exit(1)


input_folder = sys.argv[1]
output_folder = sys.argv[2]

#create a folder for the output (output_folder), if it already exists, don't throw an error

os.makedirs(output_folder, exist_ok=True)

#core loop

for filename in os.listdir(input_folder):

    if filename.lower().endswith(".pdf"):

        input_pdf = os.path.join(input_folder, filename)
        output_pdf = os.path.join(output_folder, filename)

        old_pdf = fitz.open(input_pdf)
        new_pdf = fitz.open()

        for page in old_pdf:
            pix = page.get_pixmap()

            new_page = new_pdf.new_page(
                width=pix.width,
                height=pix.height
            )

            new_page.insert_image(
                new_page.rect,
                pixmap=pix
            )

        new_pdf.save(output_pdf)

        old_pdf.close()
        new_pdf.close()



print("PDF flattening complete")  #confirming script ran successfully
