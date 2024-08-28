#Program to count no. of characters in given line
str=input("Enter any string:")
num=0
lower=0
upper=0
for i in range (len(str)):
  if (str[i].isupper ()):
    upper+=1
  elif(str[i].isdigit()):
    num+=1
  elif(str[i].islower()):
    lower+=1
print("No. of digits are:",num)
print("No. of lowercases are:",lower)
print("No. of uppercases are:",upper)
