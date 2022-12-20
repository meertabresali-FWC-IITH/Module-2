import numpy as np                 #Can be done easily using Numpy Lib

array=np.array([3,4.5,3 + 5j,0])   #Initialize complex array

real=np.isreal(array)              #Boolean condition for real part

real_array=array[real]             #Storing it in variable using boolean indexing

imag=np.iscomplex(array)           #Boolean condition for real part

imag_array=array[imag]             #Storing it in variable using boolean indexing


print("real=", real)
print("imag=", imag)
print("real_array=", real_array)
print("imag_array=", imag_array)



z = complex(5, 7)
print("Output=z = complex(5, 7)=:", z)

r=np.real(z)
print("real=", r)

i=np.imag(z)
print("image=", i)




# Output: (5+7j) 





z = complex(3)
print("Output=z = complex(3):", z)
# Output: (3+0j)


z = complex()
print("Output=z = complex():", z)
# Output: 0j

z = complex('1+1j')
print("Output=z = complex('1+1j'):", z)
# Output: 1+1j

z = complex(1, -4)
print("Output=z = complex(1, -4):", z)
# Output: 1-4j





