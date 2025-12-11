import numpy as np

# Example signal
x = np.array([1, 2, 3, 4], dtype=complex)  # length = 4
N = len(x)  # DFT length

# Prepare k and n indices
n = np.arange(N)
k = np.arange(N)

# Sampling frequencies for DFT
omega_k = 2 * np.pi * k / N

# DTFT sampling (manual computation)
X = np.zeros(N, dtype=complex)
for i in range(N):
    X[i] = np.sum(x * np.exp(-1j * omega_k[i] * n))

print("DFT via DTFT sampling:")
print(X)

# Check with numpy's fft for verification
print("Numpy FFT:", np.fft.fft(x))
