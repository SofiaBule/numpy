import numpy as np

def fft(signal):
    N = len(signal)
    if N <= 1:
        return signal
    even = fft(signal[0::2])
    odd = fft(signal[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([even + factor[:N//2] * odd, even + factor[N//2:] * odd])

# Example usage:
signal = np.array([0, 1, 2, 3])
transformed_signal = fft(signal)
print("FFT result:", transformed_signal)
