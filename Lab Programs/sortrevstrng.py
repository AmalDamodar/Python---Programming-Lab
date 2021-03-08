a=input("\nEnter a string\n")
z=a.split()
z.sort(reverse=True,key=len)
print(z)
