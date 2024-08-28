#Enter the first alphabet to search record
import csv
def search():
  file=open("info p18.csv","r")
  R=csv.reader(file)
  a=input("alphabet to be searched").lower()
  for i in R:
    if i[0][0] in a:
      print(i)
  file.close()
search()
