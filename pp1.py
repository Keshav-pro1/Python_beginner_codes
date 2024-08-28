n=int(input(" power n="))
x=int(input(" base x="))
p=1
s=1
for i in range(1,n+1):
	p=p*x 
	s=s+p
print (s)
