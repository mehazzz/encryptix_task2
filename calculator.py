def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return(a/b)

x = int(input("enter num1: "))
y = int(input("enter num2: "))
c=input("enter choice(+/-/*//: ")

if c == '+':
    r=add(x,y)
    print(r)
elif c == '-':
    r=sub(x,y)
    print(r)
elif c == '*':
    r=mul(x,y)
    print(r)
else:
    r=div(x,y)
    print(r)




