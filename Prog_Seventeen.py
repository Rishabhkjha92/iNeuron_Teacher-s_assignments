#17. WAF to read a Word file

import docx

def readnow(filed):
    doc = docx.Document(filed)
    li_lis = []
    for i in doc.paragraphs:
        li_lis.append(i.text)
    print("The output is :\n",li_lis)
        
filed_1="C:\Users\Dell\Downloads\Sample RCA.docx"
readnow(filed_1)