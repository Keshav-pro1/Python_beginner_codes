#Writing CSV Data
import csv
def createcsv():
  data = []
  while True:
    name= input("Enter a name (or 'q' to quit): ")
    if name == 'q':
      break
    age = input("Enter an age: ")
    data.append([name, age])
  with open('info p18.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
  print("Data written successfully!")
createcsv()

