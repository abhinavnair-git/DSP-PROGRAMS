import numpy as np
import matplotlib.pyplot as plt

# FIR Low Pass Filter design using manually constructed Hanning window
N = 101  # Filter length
fc = .25  # Normalized cutoff frequency (0 to 0.5)

#  Hanning window 
n = np.arange(N)
hanning_window = 0.5 - 0.5 * np.cos(2 * np.pi * n / (N - 1))

# Ideal low-pass filter (sinc)
n_centered = n - (N - 1) / 2
h_ideal = 2 * fc * np.sinc(2 * fc * n_centered)

# Apply window to ideal response
h = h_ideal * hanning_window

# Compute frequency response using FFT
fft_size = 512
H = np.fft.fft(h, fft_size)
H_mag = np.abs(H[:fft_size // 2])  # Positive frequencies only
freq = np.linspace(0, 0.5, fft_size // 2)  # Normalized frequency
Hdb=20*np.log10(H_mag/np.max(H_mag))

# Plot frequency response
plt.plot(freq, Hdb, 'b', linewidth=2)
plt.title('Frequency Response of FIR Low-Pass Filter (Hanning Window, N=11)')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude |H(f)|')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
