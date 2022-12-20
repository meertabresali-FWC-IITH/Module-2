import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if
import soundfile as sf
from scipy import signal

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

#Coefficients
a0= 1
a1=-0.54688232  

   
b0= 0.22655884
b1= 0.22655884 


#defining impulse sequence  
k = 100
h = np.zeros(k)

#printing initial impulse sequence
print("initial h(n)=")
print(h)
print("-----------------------------------------------")
print("length of intial h(n)=", len(h))
print("-----------------------------------------------")

h[0] = b0
h[1] = a1*h[0]+b1

for n in range(2,k-1):
		h[n] = a1*h[n-1]
		
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

















