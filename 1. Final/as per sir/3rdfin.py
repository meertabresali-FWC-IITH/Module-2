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
x=input_signal

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



#printing initial impulse sequence
print("initial h(n)=")
print(h)
print("-----------------------------------------------")
print("length of intial h(n)=", len(h))
print("-----------------------------------------------")



v= 0.0140997 #for n<=0
h[0]=v
for n in range(1,k):
		p=(0.640832 - 3.68314*10**(-17)*1j) * 0.546882**n - (0.29095 - 0.141431*1j) * (0.663072 - 0.36799*1j)**n - (0.29095 + 0.141431*1j) *(0.663072 + 0.36799*1j)**n #for n>0
		h[n]=p.real




print("Impulse h(n)=")
print(h)
print("-----------------------------------------------")
#print("length of impulse h(n)=", len(h))
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































