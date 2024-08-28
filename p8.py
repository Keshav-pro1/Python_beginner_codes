#Program for sum of all elements in list
def sumlist(list):
    s=0
    for i in range(len(list)):
        s = s+list[i]
    return s
list = eval(input("Enter list:"))
print(list)
print("sum of list: ",sumlist(list))
