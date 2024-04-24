
import re
import random
import PyPDF2

counterFile = open("C:\Projects\ConvertPDF\\numberPDF.txt","r")
numberPDFs = int(counterFile.read())
counterFile.close()
counterFile = open("C:\Projects\ConvertPDF\\numberPDF.txt","w")
counterFile.write(str(numberPDFs + 1))
counterFile.close()


pdfName = "pdf1"
pdf = open("C:\Projects\ConvertPDF\\" + pdfName + ".pdf","rb")
pdfreader = PyPDF2.PdfReader(pdf)
x = len(pdfreader.pages)
pdf = pdfreader.pages[0]
text = pdf.extract_text()


textDocPath = "C:\Projects\ConvertPDF\\TextOutput" + str(numberPDFs) + "_From_" + pdfName + ".txt"

file1 = open(textDocPath,"a")
file1.writelines(text)
file1.close()



