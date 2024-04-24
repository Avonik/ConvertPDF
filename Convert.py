import re
import os
import random
import PyPDF2
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    app.config['UPLOAD_FOLDER'] = 'C:\Projects\ConvertPDF\\venv\\UPLOAD_FOLDER'
    uploaded_file = request.files['avatar']
    if uploaded_file.filename != '':
        pdf_name = uploaded_file.filename[:-4]  # Remove the ".pdf" extension from the filename
        pdf_folder = "uploaded_pdfs"

        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], pdf_name + ".pdf"))
        resultText = ReadPDFandOutput(pdf_name)
        return str(resultText)
    return "No file selected!"



def ReadPDFandOutput(pdfName):
    #get number of pdf print
    counterFile = open("C:\Projects\ConvertPDF\\numberPDF.txt", "r")
    numberPDFs = int(counterFile.read())
    counterFile.close()
    counterFile = open("C:\Projects\ConvertPDF\\numberPDF.txt", "w")
    counterFile.write(str(numberPDFs + 1))
    counterFile.close()


    pdf = open("C:\Projects\ConvertPDF\\venv\\UPLOAD_FOLDER\\" + pdfName + ".pdf","rb")
    pdfreader = PyPDF2.PdfReader(pdf)
    x = len(pdfreader.pages)
    result = []

    for i in range(0,x-1):
        selected_page = pdfreader.pages[i]
        text = selected_page.extract_text()
        result.append(text)



    textDocPath = "C:\Projects\ConvertPDF\\TextOutput" + str(numberPDFs) + "_From_" + pdfName + ".txt"

    file1 = open(textDocPath, "a", encoding="utf-8")
    file1.writelines(result)
    file1.close()

    return result

if __name__ == '__main__':
    app.run(debug=True)

