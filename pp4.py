a=int(input("ENTER no.1="))
b=int(input("ENTER no.2="))
c=int(input("ENTER no.3="))
d=int(input("ENTER no.4="))
e=int(input("ENTER no.5="))
f=int(input("ENTER no.6="))
x=a+b+c+d+e+f

for i in range (x):
  if i==a or i==b or i==c or i==d or i==e or i==f:
    print(i)
  else:
    continue
