#Program to remove all odd no.
def removeodd(l):
  for i in l:
    if i%2!=0:
      l.remove(i)
  print (l)
removeodd([1,2,3,4,5])
removeodd([22,23,56,79])
