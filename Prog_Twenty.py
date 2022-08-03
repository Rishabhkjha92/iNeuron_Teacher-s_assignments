from os import listdir
from PyPDF3 import PdfMerger
import click

click.clear()

merg = PdfMerger()

loc = "" #directory's lcoation

for file in listdir(loc):
    if file.endswith(".pdf"):
        merg.append(file)
        
merg.write("Result.pdf")
merg.close()
    