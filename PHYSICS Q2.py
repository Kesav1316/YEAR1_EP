import numpy as np
import matplotlib.pyplot as plt

f = 286.0  #Setting roll number as frequency

#Number of waves
num_cycles = 10  

#Time array
t = np.linspace(0, num_cycles * (1.0 / f), 10000)

#Empty array for square 
square_wave = np.zeros_like(t)

#Empty array for saw tooth
sawtooth_wave = np.zeros_like(t)

#Empty array for triangle
triangle_wave = np.zeros_like(t, dtype=np.float64)  # Ensure real dtype

#Number of overtones
n_max_square = 10000 
n_max_sawtooth = 1000 
n_max_triangle = 1000  

#SQUARE WAVE
for n in range(1, n_max_square, 2):
    square_wave += (1/n) * np.sin(2 * np.pi * n * f * t)

square_wave *= (4/np.pi)

#SAW TOOTH WAVE
for i in range(1,n_max_sawtooth):
    frequency = i * f
    harmonic = ((-1) ** i) * (np.sin(2 * np.pi * frequency * t) / i)
    sawtooth_wave += harmonic

sawtooth_wave *= (2 / np.pi)

#TRIANGLE WAVE
for n in range(1, n_max_triangle + 1):
    harmonic = (((-1) ** ((n - 1)/2)) / (n ** 2)) * np.sin(2 * np.pi * f * n * t)
    triangle_wave += np.real(harmonic)

triangle_wave *= 8 / (np.pi ** 2)
triangle_wave = np.real(triangle_wave)


plt.figure(figsize=(12, 8))

#PLOTTING SQUARE WAVE
plt.subplot(3, 1, 1)
plt.plot(t, square_wave)
plt.title("Square Wave(y = a/n * sin(2*pi*n*f*t))")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-1.2, 1.2)
plt.xlim(0.000,0.035)

#PLOTTING SAW TOOTH WAVE
plt.subplot(3, 1, 2)
plt.plot(t, sawtooth_wave)
plt.title("Sawtooth Wave(y = 2a/pi * Σ((-1)^n)*(sin(2*pi*n*f*t)/n)))")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-1.2, 1.2)
plt.xlim(0.000,0.035)

#PLOTTING TRIANGLE WAVE
plt.subplot(3, 1, 3)
plt.plot(t, triangle_wave)
plt.title("Triangle Wave(8/pi^2 * Σ ((-1)^(n-1)/2)/n^2 * sin(2*pi*f*n*t))")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-1.2, 1.2)
plt.xlim(0.000,0.035)


plt.tight_layout()

plt.show()