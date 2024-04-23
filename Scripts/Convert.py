import re
from pdfminer.high_level import extract_text, extract_text

#text = extract_text("C:\Projects\ConvertPDF\pdf1.pdf")

import PyPDF2

pdf = open('C:\Projects\ConvertPDF\pdf1.pdf','rb')
pdfreader = PyPDF2.PdfReader(pdf)
x = len(pdfreader.pages)
pdf = pdfreader.pages[0]
text = pdf.extract_text()



file1 = open(r"C:\Projects\ConvertPDF\\TextOutput.txt","a")
file1.writelines(text)
file1.close()

