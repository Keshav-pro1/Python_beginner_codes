#AVERAGE,MAX. , MIN., MARKS
a=int(input("how many students="))
z=[]
for i in range (a):
  b=int(input("MARKS OF STUDENT ="))
  z.append(b)
print("List of marks of students=",z)
avg=(sum(z))/a
print("Average marks of students=",avg)
m=max(z)
print("Maximum marks of a student=",m)
l=min(z)
print("Minimum marks of a student=",l)
