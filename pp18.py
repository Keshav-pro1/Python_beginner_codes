#counting no. whose 1st and last words are same
a=eval(input("ENTER THE LIST"))
c=0
for i in a:
  k=[]
  k.append(i)
  if k[0][0]==k[0][-1]:
    c+=1
print(c)
