import statistics
print("1. Mean    2.Median    3.Mode  ")
z=0
a=eval(input("data in list form"))
b=input("your choice").lower()
if b=="mean":
  z=statistics.mean(a)
elif b=="median":
  z=statistics.median(a)
elif b=="mode":
  z=statistics.mode(a)
else:
  
  print("INVALID")
b.upper()
print(b,"=",z)
