a=int(input("Enter element 1\n"))
b=int(input("Enter element 2\n"))

o=(input("Enter the operand \n+\n-\n*\n/\n"))

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

if(o=='+'):
    print(add(a,b))
elif o=='-':
    print(sub(a,b))
elif(o=='*'):
    print(mul(a,b))
elif(o=='/'):
    print(div(a,b))
else:
    print("\nInvalid")
