import numpy as np 
import matplotlib.pyplot as plt

#Time domain signal
t = np.arange(0,10,0.1) #Time vector
x = np.sin(t) #Sample signal

#Compute Fourier transform
X = np.fft.fft(x)

#Compute frequency axis
fs = 1/(t[1] - t[0]) #Sampling frequency
f = np.arange(-fs/2,fs/2,fs/len(x)) #Frequency axis

#Plot the magnitude spectrum
plt.plot(f,np.abs(np.fft.fftshift(X)))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Fourier Transform")
plt.show()

