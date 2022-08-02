# 16. WAF to read a complete PDF file
# install pyPDF3 first of all --> pip3 install pyPDF3

import PyPDF2 as py
import click
  
pdfob = open('C:\Users\Dell\Downloads\Form16.pdf', 'rb')
  
pdfrdr = PyPDF2.PdfFileReader(pdfob)
print(pdfrdr.numPages)
for i in range(0,pdfrdr.numPages):
    pgob = pdfrdr.getPage(0)
    data = pgob.extractText()
    print(data)
pdfob.close()
