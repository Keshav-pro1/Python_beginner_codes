#Program to find Rate constant
import math
A=float(input('A:'))
T1=float(input('T:'))
E=float(input('Ea:'))
k=-E/(8.314*T1)
z=A*(math.exp(k))
print("Rate const.=",z)
