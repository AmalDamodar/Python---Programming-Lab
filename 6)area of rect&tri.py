width = float(input('Width of Rectangle: '))
height = float(input('Height of Rectangle: '))
rArea = width * height

a = float(input('\nFirst side of Triangle: '))  
b = float(input('Second side of Triangle: '))  
c = float(input('Third side of Triangle: ')) 
s = (a + b + c) / 2    
tArea = (s*(s-a)*(s-b)*(s-c)) ** 0.5
 
print("\nArea of the Rectangle is %0.2f" %rArea)
print("Area of the Triangle is %0.2f" %tArea) 
