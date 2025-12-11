import numpy as np
import matplotlib.pyplot as plt
def dft(x):
    x=np.asarray(x)  
    N=len(x)
    X=np.zeros(N)  
    for k in range(N):
        for n in range(N):
           angle=-2j*np.pi*k*n/N
           X[k]+=x[n]*np.exp(angle)          
    return X
x=[1,2,3,4]
result=dft(x)
print(result)
plt.subplot(2,1,1)
plt.stem(x)
plt.title('input')
plt.subplot(2,1,2)
plt.stem(result)
plt.title('dft')
plt.tight_layout()
plt.show()

