
"""
PDF Automation Toolkit

A collection of Python tools for PDF workflow automation.

Created by ipvl
"""


#import pip modules

import sys
from pypdf import PdfReader

#point variable to pdf

pdf_file = sys.argv[1]

#read the pdf & fields

reader = PdfReader(pdf_file)
fields = reader.get_fields()

#print fields

if fields:
    for field_name, field_info in fields.items():
        print(field_name)
else:
    print("No form fields found")
