import numpy as np
import matplotlib.pyplot as plt
x=eval(input("Enter the input"))
N=int(input("enter dft size"))
def dft_matrix(x):
    x = np.array(x, dtype="complex")
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    X = W @ x
    return X
X_dft=dft_matrix(x)
X_padded=np.zeros(N)
X_padded=np.pad(x,(0,N-len(x)))
X_dtft=dft_matrix(X_padded)
print("DFT")
print(np.round(X_dft,3))
print("Dtft")
print(np.round(np.real((X_dtft))))
plt.subplot(2,1,1)
plt.stem(np.abs(np.round(X_dft)))
plt.subplot(2,1,2)
plt.stem(np.abs(np.round(X_dtft)))
plt.show()