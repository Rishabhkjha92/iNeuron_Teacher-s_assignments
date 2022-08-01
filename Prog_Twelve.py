# 12. WAF which can move a file from one directory to another directory

import os, shutil, click
from turtle import ScrolledCanvas

click.clear()

src = r"C:\Users\Dell\VSCode\Python\Playing around\iNeuron\Holiday_Task\\"
dest = r"C:\Users\Dell\VSCode\Python\Playing around\iNeuron\OhOhOh\\"
f_name = "Prog_Three.py"


#check if the src file exists in the destination folder
if os.path.exists(dest+f_name):
    var = os.path.splitext(f_name) #splitext will split the file name in parts depending on '.' dot
    name = var[0]
    ext = var[1] #hoping there is only 1 '.' in the name
    new_name = name+"_1"+ext
    shutil(src+f_name,dest+new_name)
else :
    shutil.copy(src+f_name,dest+f_name) #in case you don't want to move but oly copy

    