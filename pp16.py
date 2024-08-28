#Replace vowels to uppercase
z=input("STRING=").lower()
a=' '
for i in z:
  if i in "aeiou":
    a+= i.upper()
  else:
    a+=i
print("ORIGINAL STRING=",z)
print("NEW STRING=",a)
