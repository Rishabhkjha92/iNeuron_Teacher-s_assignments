#   Program - 2
#Write function to print index of all primitive elements
# Primitive Elements in Python
# Integer, Float, String, Boolean
import click
click.clear()
int_index=[]
float_index=[]
string_index=[]
boolean_index=[]
lili = ['1',2,1,4.2,"different values",2.2,False,True,True,True,"String value"]
def func(li_li):
    pos = 0
    for i in li_li:
        if type(i) == int:
#            st = str(i)
#            st = "%s" %i
            int_index.append(pos)
            int_index.append(i)
            pos+=1
        elif type(i) == float:
            float_index.append(pos)
            float_index.append(i)
            pos+=1
        elif type(i) == str:
            string_index.append(pos)
            string_index.append(i)
            pos+=1
        elif type(i) == bool:
            boolean_index.append(pos)
            boolean_index.append(i)
            pos+=1

            


func(lili)
print("Integer elements and their indexes : ",int_index)
print("Float elements and their indexes : ",float_index)
print("Boolean elements and their indexes : ",boolean_index)
print("String elements and their indexes : ",string_index)