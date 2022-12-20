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



#Partial fractions coefficients
A= (-11609.81260855773+4808.941839074765j)
B= (11609.81260855774-28028.567056190215j)
C= (11609.812608557711+28028.567056190244j)
D= (-11609.812608557728-4808.941839074786j)

#exponentail terms of h(n)
exp_aT= (0.6951503468473601+0.40405937455645385j)
exp_bT= (0.5766641397062453+0.12779886073731517j)
exp_cT= (0.5766641397062454-0.12779886073731508j)
exp_dT= (0.6951503468473598-0.4040593745564536j)

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

















