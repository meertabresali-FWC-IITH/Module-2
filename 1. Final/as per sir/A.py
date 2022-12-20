import numpy as np
#import cmath for complex number operations
import cmath


wc=2*np.pi*4000
print("wc=", wc)

e5=cmath.exp(5*np.pi*0.125*(0+1j))
e7=cmath.exp(7*np.pi*0.125*(0+1j))
e9=cmath.exp(9*np.pi*0.125*(0+1j))
e11=cmath.exp(11*np.pi*0.125*(0+1j))

e57=e5-e7
e59=e5-e9
e511=e5-e11

e75=e7-e5
e79=e7-e9
e711=e7-e11

e95=e9-e5
e97=e9-e7
e911=e9-e11

e115=e11-e5
e117=e11-e7
e119=e11-e9

A=wc/(e57*e59*e511)
B=wc/(e75*e79*e711)
C=wc/(e95*e97*e911)
D=wc/(e115*e117*e119)
print("----------------------------")
print("Exponential terms into coplex numbers")
print("e5=", e5)
print("e7=", e7)
print("e9=", e9)
print("e11=", e11)
print("e5-e7=", e57)
print("e5-e9=", e59)
print("e5-e11=", e511)
print("----------------------------")
print("Partial fractions coefficients")
print("A=", A)
print("B=", B)
print("C=", C)
print("D=", D)
print("----------------------------")
print("Roots of H(s)")
a=(wc*e5)
b=(wc*e7)
c=(wc*e9)
d=(wc*e11)

print("a=", (wc*e5))
print("b=", (wc*e7))
print("c=", (wc*e9))
print("d=", (wc*e11))
print("----------------------------")
T=1/44100
print("Sampling Time, T=", T)
print("----------------------------")
print("exponentail terms of h(n)")
eaT = cmath.exp(a*T)
ebT = cmath.exp(b*T)
ecT = cmath.exp(c*T)
edT = cmath.exp(d*T)
print("exp(aT)=", eaT)
print("exp(bT)=", ebT)
print("exp(cT)=", ecT)
print("exp(dT)=", edT)

hn0=np.real(A+B+C+D)
print("hn0=", hn0)
hn1=np.real(A*eaT+B*ebT+C*ecT+D*edT)
print("hn1=", hn1)
hn2=np.real(A*eaT**2+B*ebT**2+C*ecT**2+D*edT**2)
print("hn2=", hn2)
hn3=np.real(A*eaT**3+B*ebT**3+C*ecT**3+D*edT**3)
print("hn3=", hn3)

p=(A*T)/(2-a*T)
k=(2+a*T)/(2-a*T)
print("p=", p)
print("k=", k)

