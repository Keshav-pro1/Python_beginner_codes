a=int(input("Enter no."))
b=int(input("Enter no."))
c=input("operator=")
z=0
if c=='+':
  z=a+b
elif c=='-':
  z=a-b
elif c=='*':
  z=a*b
elif c=='/':
  z=a/b
elif c=='//':
  z=a//b
elif c=='%':
  z=a%b
elif c=='**':
  z=a**b

print(z) 
