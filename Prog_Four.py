import click

click.clear()

def func1(func):
    a = func()
    return a

def func2 ():
    val = input("Enter the value :\t")
    return val
    
g = func1(func2)
print("The value entered is :\t",g)