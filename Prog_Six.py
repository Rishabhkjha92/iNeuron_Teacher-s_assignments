import click
click.clear()

li=[]
count=0
def func(n):
    for i in range(n):
        v = input("Enter the value for list :\t")
        li.append(v)

def returning_list():
    for i in range(n):
        print("Position ",i," : ","Value ",li[i])
    
n = int(input("Enter the number of elements the user want : "))
func(n)
returning_list()