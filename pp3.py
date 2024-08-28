n=int(input("No.of series="))
a=0
b=1
for i in range (n//2):
	print(a)
	print(b)
	a=a+b
	b=a+b
