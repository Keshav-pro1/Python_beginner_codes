#Finding data from tuple

M=eval(input("Enter  the marks "))
M1= int(input("enter any marks to search"))
A=0
for i in M:
    if i==M1:
        A=1
        break
    else:
      continue
if A==1:
    print("found")
else:
    print("not found")
