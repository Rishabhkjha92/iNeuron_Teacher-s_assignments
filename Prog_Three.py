import click

click.clear()

dicct = {}

def fun(n):
    global dicct 
    dicct = dict(input().split(" ",1) for _ in range(n))
    print("\nThe Dictionary is : \n\t")
    print(dicct)
     
n = int(input("Enter the range for numbers :\t"))        
fun(n)

print("\nThe Dictionary is : \t")
for i,j in dicct.items():
    print(i," : ",j)

print("Now for LIST\n")
li = [(i,j) for i,j in dicct.items()]
print(li)