a=int(input("No."))
b=0
for i in range (2,a):
  if a%i==0:
    b=1
    break
  else:
    continue

if b==0:
  print("Prime no.")
elif b==1:
  print ("No. is composite")
