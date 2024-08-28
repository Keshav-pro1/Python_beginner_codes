#Searching info from one file
import pickle
def search():
  f=open("info p16.dat","rb")
  r=int(input("your adm.no."))
  rec=pickle.load(f)
  rec1=pickle.load(f)
  rec2=pickle.load(f)
  print(rec,rec1,rec2)
  full=[rec,rec1,rec2]
  z=0
  for i in full:
    if i[0]== r:
      print ("Found-->",i)
      z=1
      break
  if z==0:
    print ("data not found |:(|")
  f.close()
search()
