import numpy as np
import matplotlib.pyplot as plt
def dit_fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = dit_fft(x[::2])
    odd = dit_fft(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    X = [even[k] + T[k] for k in range(N // 2)] + \
    [even[k] - T[k] for k in range(N // 2)]
    return np.asarray(X,dtype='complex')
x = eval(input('x:'))
result = dit_fft(x)
print("FFT using DIT:", result)