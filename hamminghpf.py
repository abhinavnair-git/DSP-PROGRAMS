import numpy as np
import matplotlib.pyplot as plt

# FIR High-Pass Filter design using Hamming window and sinc formulation
N = 101          # Filter length
fc = 0.25       # Normalized cutoff frequency (0 to 0.5)

# Generate indices
n = np.arange(N)
n_centered = n - (N - 1) / 2  # Center indices

# Ideal low-pass filter impulse response (using sinc)
h_ideal_lp = 2 * fc * np.sinc(2 * fc * n_centered)

# Convert to high-pass using spectral inversion: h_hp[n] = delta[n] - h_lp[n]
delta = np.zeros(N)
delta[int((N - 1) / 2)] = 1
h_ideal_hp = delta - h_ideal_lp

# Generate Hamming window manually
hamming_window = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

# Apply window to ideal high-pass response
h = h_ideal_hp * hamming_window

# Compute frequency response using FFT
fft_size = 512
H = np.fft.fft(h, fft_size)
H_mag = np.abs(H[:256])  # Positive frequencies only
freq = np.linspace(0, 0.5, 256)
Hdb=20*np.log10(H_mag/np.max(H_mag))

# Plot frequency response
plt.plot(freq, Hdb, 'r', linewidth=2)
plt.title('Frequency Response of FIR High-Pass Filter (Hamming Window, N=11)')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('|H(f)|')
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.show()

print("FIR Coefficients:")
print(np.round(h, 5))
