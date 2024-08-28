#Program to find activation energy
import math
K1=float(input('K1:'))
T1=float(input('T1:'))
K2=float(input('K2:'))
T2=float(input('T2:'))
a=(8.314*2)*(T1*T2)
b=math.log(K1)-math.log(K2)
c=(T1-T2)*8.314
E=(a*b)/c
E=round(E,3)
print("Activation energy=",E)
