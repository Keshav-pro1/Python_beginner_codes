#Appending data in binary file
import pickle
def binwrite():
  f=open("info p15.dat","wb")
  a="y"
  while a=="y":
    r=eval(input("Enter your name="))
    pickle .dump(r,f)
    a=input("more?(y/n)=")
  f.close()
binwrite()
  

