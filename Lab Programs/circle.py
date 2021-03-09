import math

def area(r):
    return math.pi*r*r

def per(r):
    return 2*math.pi*r

r=int(input("\nEnter Radius\n"))

print("Area Of the Circle",area(r))
print("\nPerimeter of the Circle",per(r))