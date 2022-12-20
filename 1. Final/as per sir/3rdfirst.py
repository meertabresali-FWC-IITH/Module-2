import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
import soundfile as sf
from scipy import signal

import cmath


input_signal,fs = sf.read('filter_codes_Sound_Noise.wav')
#sampling frequency of Input signal
sampl_freq=fs
x=input_signal[:100]

print("input sequence x(n)=")
print(x)
print("-----------------------------------------------")
print("length of input sequence lx=", len(x))
print("-----------------------------------------------")
print("Sampling frequency fs=", fs)
print("-----------------------------------------------")


#defining impulse sequence  
k = 100
h = np.zeros(k)

#Sampling time
T=1/44100 

#printing initial impulse sequence
print("initial h(n)=")
print(h)
print("-----------------------------------------------")
print("length of intial h(n)=", len(h))
print("-----------------------------------------------")



h[0]= np.real(0.0140997 - 8.1037*(10**(-19))*1j) - (5.55112*10**(-17)*1j) (0.663072 - 0.36799*1j)**0 #for n<=0

for n in range(1,k-1):
		h[n]=np.real(0.640832 - 3.68314*10**(-17)*1j) * 0.546882**n - (0.29095 - 0.141431*1j) * (0.663072 - 0.36799*1j)**n - (0.29095 + 0.141431*1j) *(0.663072 + 0.36799*1j)**n #for n>0




print("Impulse h(n)=")
print(h)
print("-----------------------------------------------")
print("length of impulse h(n)=", len(h))
print("-----------------------------------------------")

#finding output sequence by convolution operation
y=np.convolve(x,h)

print("output sequence y(n)")
print(y)
print("-----------------------------------------------")
print("length of output sequence y(n) =", len(y))
print("-----------------------------------------------")

#writing output sequence into noise wav
sf.write('Sound With ReducedNoise.wav', y, fs)

#subplots
#plt.subplot(2, 1, 1)
#plt.stem(range(0,len(x)),x)
#plt.title('Digital Input-Audio')
#plt.ylabel('$x(n)$')
#plt.grid()# minor


#plt.subplot(2, 1, 2)
plt.stem(range(0,k),h)
plt.title('Butterworth filter - impulse sequence')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor


plt.show()




































for n in range(0,k-1):
		h[n] = [((A*(exp_aT)**n+B*(exp_bT)**n+C*(exp_cT)**n+D*(exp_dT)**n))]
		
print("Impulse h(n)=")
print(h)
print("-----------------------------------------------")
print("length of impulse h(n)=", len(h))
print("-----------------------------------------------")

#finding output sequence by convolution operation
y=np.convolve(x,h)

#print("output sequence y(n)")
#print(y)
#print("-----------------------------------------------")
#print("length of output sequence y(n) =", len(y))
#print("-----------------------------------------------")

#writing output sequence into noise wav
sf.write('Sound With ReducedNoise.wav', y, fs)

#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,len(x)),x)
plt.title('Digital Input-Audio')
plt.ylabel('$x(n)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.stem(range(0,k),h)
plt.title('Butterworth filter - impulse sequence')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor


plt.show()

















