import numpy as np
import matplotlib.pyplot as plt

# Define the fundamental frequency (f)
f = 286.0  # Example: A4 note (440 Hz)

# Define the number of cycles (periods)
num_cycles = 10  # Increase this value to have more cycles

# Define the number of terms in the summation (increase for sharper wave)
n_max = 1000  # You can increase this value for sharper transitions

# Define the amplitude of the triangle wave
A_triangle = 1.0  # You can change this value as needed

# Calculate the time period of the fundamental frequency
T = 1.0 / f

# Calculate the total time duration needed for the specified number of cycles
total_duration = num_cycles * T

# Create a time array with higher precision
t = np.linspace(0, total_duration, 10000)

# Initialize an empty array for the triangle wave
triangle_wave = np.zeros_like(t, dtype=np.float64)  # Ensure real dtype

# Calculate the triangle wave using the provided equation with a loop
for n in range(1, n_max + 1):
    harmonic = (((-1) ** ((n - 1)/2)) / (n ** 2)) * np.sin(2 * np.pi * f * n * t)
    triangle_wave += np.real(harmonic)

# Multiply by (8/π^2) to adjust amplitude, and then by A_triangle
triangle_wave *= 8 / (np.pi ** 2)

# Ensure the result is real (remove any residual imaginary part)
triangle_wave = np.real(triangle_wave)

# Plot the triangle wave with the provided equation
plt.figure(figsize=(10, 4))
plt.plot(t, triangle_wave)
plt.title(f"Triangle Wave with {num_cycles} Cycles, Amplitude {A_triangle}, Sharp Edges (n_max = {n_max})")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.ylim(-A_triangle * 1.2, A_triangle * 1.2)  # Adjust the y-axis limits as needed
plt.show()


