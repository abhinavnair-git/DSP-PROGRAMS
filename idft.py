import numpy as np

def idft(X):
    X = np.asarray(X, dtype=complex)
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
    return np.real(x / N)  # only real part

# Correct DFT of [1, 2, 3, 4]
X = [10+0j, -2+2j, -2+0j, -2-2j]

print(idft(X))
