
import numpy as np
import matplotlib.pyplot as plt

# Define the fundamental frequency (c)
c = 286.0  # Example: A4 note (440 Hz)

# Define the number of cycles
num_cycles = 20  # Increase this value to have more cycles

# Define the number of overtones
n_max = 10  # You can increase this value to add more overtones

# Calculate the time period of the fundamental frequency
T = 1.0 / c

# Calculate the total time duration needed for the specified number of cycles
total_duration = num_cycles * T

# Create a time array with higher precision
t = np.linspace(0, total_duration, 10000)

# Define the amplitude of the fundamental frequency (A)
A = 1.0  # You can change this value as needed

# Initialize an empty array for the sawtooth wave
sawtooth_wave = np.zeros_like(t)

# Calculate the sawtooth wave using the provided equation with cycles and overtones
for i in range(1, n_max + 1):
    frequency = i * c
    harmonic = ((-1) ** i) * (np.sin(2 * np.pi * frequency * t) / i)
    sawtooth_wave += harmonic

# Multiply by (2A/π) to adjust amplitude
sawtooth_wave *= (2 * A / np.pi)

# Plot the sawtooth wave with cycles and overtones
plt.figure(figsize=(10, 4))
plt.plot(t, sawtooth_wave)
plt.title(f"Sawtooth Wave with {num_cycles} Cycles and {n_max} Overtones using Provided Equation")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-1.2, 1.2)  # Adjust the y-axis limits as needed
plt.show()

