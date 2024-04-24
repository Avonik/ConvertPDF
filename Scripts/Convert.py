
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
result = []

for i in range(0,x-1):
    selected_page = pdfreader.pages[i]
    text = selected_page.extract_text()
    result.append(text)

print(str(result))

textDocPath = "C:\Projects\ConvertPDF\\TextOutput" + str(numberPDFs) + "_From_" + pdfName + ".txt"

file1 = open(textDocPath, "a", encoding="utf-8")
file1.writelines(result)
file1.close()



