import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbols="!@#$%^&*()_+:?~"

all = lower+upper+number+symbols

length=8
password= "".join(random.sample(all,length))
print("PASSWORD GENERATOR")
print("++++++++++++++++++")
print("The Generated Passowrd is =>",password)