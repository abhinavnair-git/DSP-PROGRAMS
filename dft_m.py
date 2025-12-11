import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    x = np.asarray(x, dtype=complex)  
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))          
    w = np.exp(-2j * np.pi * k * n / N)
    X = w @ x                        
    return X

x = [1, 2, 3]
result = dft(x)
print(np.real(result))
plt.subplot(2, 1, 1)
plt.stem(x)
plt.title('Input Sequence')

plt.subplot(2, 1, 2)
plt.stem(np.abs(result))
plt.title('Magnitude of DFT')

plt.tight_layout()
plt.show()
