#REMOVE SELECTED DATA FROM LIST
a=int(input("how many no of data="))
z=[]
for i in range (a):
  d=eval(input("DATA for list ="))
  z.append(d)
x=len(z)
print("Initial list= ",z)
b=input("want to change remove any data? (yes/no) =").lower()
if b=="yes":
  c=int(input("how many no of data you want to remove="))
  if c<=x:
    for k in range (c):
      b=eval(input("Data you want to remove="))
      z.remove(b)
    print("Final list=",z)
  else:
    print("error")
elif b=="no":
  print(z)
else:
  print("INVALID INPUT ")
  
