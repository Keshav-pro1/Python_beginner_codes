# Reading and Printing CSV Data
import csv
with open('info p18.csv', 'r') as file:
  filereader = csv.reader(file)
  for row in filereader:
    name, age = row
    print(f"Name: {name}, Age: {age}")

