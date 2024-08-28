#Palindrome no.
z=input("string=")
z=z.lower()
c=0
a=0
b=len(z)-1
while a<=b:
  if z[a] != z[b] :
    c=1
    break
  else:
    a+=1
    b-=1
if c==1:
  print("NOT PALINDROME")
else:
  print("PALINDROME")
