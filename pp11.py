str=input("value name=")
a=len(str)
for x in range (1,a+1):
  for y in range (0,x):
    print(str[y],end=" ")
  print()
