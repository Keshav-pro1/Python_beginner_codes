#Change all e with a 
def pw5():
  z=open("info p14.txt","r")
  m=[]
  m1=[]
  for l in z:
    s=l.split()
    for w in s:
      if len(m1)<=15:
        m1.append(w)
      w=w.replace("e","a")
      if len(m)<=15:
        m.append(w)
  print("original    ",m1)
  print()
  print("correct    ",m)
  z.close()
pw5()
  
