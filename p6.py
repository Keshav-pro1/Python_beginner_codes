#Program to display sum of no. ending with 3
l=eval(input("list="))
s=0
for i in l:
  if i%10==3:
    s=s+i
print(s)
