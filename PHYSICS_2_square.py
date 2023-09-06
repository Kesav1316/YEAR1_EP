import numpy as np
import matplotlib.pyplot as plot

### SQUARE WAVE ###

# Initializing variables
t = np.linspace(0, 1, 10000)
square_wave = np.zeros_like(t)
frequency =286
n = 20

# Forming the square wave equation for odd 'n' harmonics
for i in range(1, n, 2):
    square_wave += (1/i) * np.sin(2 * np.pi * i * frequency * t)

square_wave *= (4/np.pi)

# Plotting the square wave
plot.figure(figsize=(15, 8))
plot.plot(t, square_wave)
plot.title("Square wave: y = (4/pi) * (1/n) * sin(2*pi*n*77*t)")
plot.xlim(0, 0.05)


plot.tight_layout()
plot.show()
