#WAF to return the name of all the files from a directory

import os,click


click.clear()
curr_path = "D:\iNeuron"
direct = os.listdir(curr_path)
print("\n\nThe files in the ",curr_path," directory are : ")
count=1
for i in direct:
    print("\n\n\t",count," - ",i)
    count+=1
    
#if looking for any special file which is ending with something just use 
# for i in direct:
# if i.endswith(".exe"):
#    dir_exe.append(i)
# print(dir_exe)
