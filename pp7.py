a=int(input("ENTER no.1="))
b=int(input("ENTER no.2="))
c=int(input("ENTER no.3="))
x=a
if x<b:
  if b>c:
    x=b
  elif c>b:
    x=c
elif x<c:
  if b>c:
    x=b
  elif c>b:
    x=c
else:
  x=a

print("Largest no. is=",x)
