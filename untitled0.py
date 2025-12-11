import numpy as np
import matplotlib.pyplot as plt
f=10
fs=50
N=50
n=np.arange(N)
x=np.sin(2*np.pi*n*f/fs)
freq=fs*n/N

X=np.fft.fft(x)
Hmag=np.abs(X)
plt.plot(freq,Hmag/N)
plt.show()


