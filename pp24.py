#If even no. comes a coin is tossed
import random
l=["HEAD","TAIL"]
a=int(input("LOWER RANGE="))
b=int(input("HIGHER RANGE="))
z=random.randint(a,b)
print(z)
if z%2==0:
  z=random.randint(0,1)
  print("coin=",l[z])
  
