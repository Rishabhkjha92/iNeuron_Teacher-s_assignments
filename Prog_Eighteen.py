# 18. WAF which can help you to filter only word file from a directory.

import os
import click 

click.clear()

loc = "" #file's location
name=[]
for file in os.listdir(loc):
    if file.endswith(".doc") or file.endswith(".docx"):
        name.append(file)
        
        
print("The list of all the Word docuemtn files in the directory are : ")
for i in name :
    print(i)
        