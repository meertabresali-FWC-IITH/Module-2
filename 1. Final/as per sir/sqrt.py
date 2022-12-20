import numpy as np
import math

fc=4000
fs=4100

g=3.41386442 
print("g=",g)
gamma=(math.cos(180*fc/fs))/(math.sin(180*fc/fs))
print("gamma=", gamma)
a=0.765366865
b=1.84775907

a0=g**4+(g**3)*(a+b)+(g**2)*(a*b+2)+g*(a+b)+1
a1=-4*g**4-2*(g**3)*(a+b)+2*g*(a+b)+4
a2=6*(g**4)-2*(g**2)*(a*b+2)+6
a3=-4*g**4+2*(g**3)*(a+b)-2*(g**1)*(a+b)+4
a4=g**4-(g**3)*(a+b)+(g**2)*(a*b+2)-g*(a+b)+1

b0=0.00345416


print("a0=", a0*b0)
print("a1=", a1*b0)
print("a2=", a2*b0)
print("a3=", a3*b0)
print("a4=", a4*b0)
