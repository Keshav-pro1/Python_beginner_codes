#Making binary file to store person information
import pickle
def createbin():
  f=open("info p16.dat","wb")
  a=int(input("how many records="))
  for i in range(a):
    no=int(input("Admission no.="))
    na=input("Name")
    ag=int(input("age"))
    cl=int(input("Class"))
    rec=[no,na,ag,cl]
    pickle.dump(rec,f)
  print("Added...........")
createbin()
