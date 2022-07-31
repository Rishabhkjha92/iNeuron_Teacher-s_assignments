import click
click.clear()
li = []
def func(n):
    for i in range(n):
        inp=input("Enter the list :\t")
        li.append(inp)
    print("The list is :")
    for i in li:
        print(i," ")
        
def concatenate_list(n):
    print("\n\n")
    for i in range(n-1):
        li[0] +=" "+li[1]
        li.pop(1)
    print(li[0])

n = int(input("Enter the number of Elements you want in the list :\t"))
func(n)
concatenate_list(n)

