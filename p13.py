#Reading text using all attributes
def READ():
   f=open("info p13.txt","r+")
   l=f.readlines(80)
   f.seek(0)
   m=f.read(6)
   f.seek(0)
   n=f.readline()
   print("readlines-->",l)
   print("read-->",m)
   print("readline-->",n)   

READ()
