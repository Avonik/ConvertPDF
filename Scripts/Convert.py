import re
import random
import PyPDF2


pdf = open('C:\Projects\ConvertPDF\pdf1.pdf','rb')
pdfreader = PyPDF2.PdfReader(pdf)
x = len(pdfreader.pages)
pdf = pdfreader.pages[0]
text = pdf.extract_text()

#randomise the path of txt to not delete old ones
rand = random.randint(0,100000)
textDocPath = "C:\Projects\ConvertPDF\\TextOutput" + str(rand) + ".txt"

file1 = open(textDocPath,"a")
file1.writelines(text)
file1.close()


