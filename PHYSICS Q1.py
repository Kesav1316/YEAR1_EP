import numpy as np
import matplotlib.pyplot as plot

time = np.linspace(0, 1,1000) # 1 second with 1000 data points

def fundamental_frequency():
    frequency = 75/2 
    amplitude = 15
    fundamental_wave = amplitude * np.sin(2 * np.pi * frequency * time)
    return fundamental_wave

def first_overtone():
    frequency = 75
    amplitude = 10
    overtone1_wave = amplitude * np.sin(2 * np.pi * frequency * time)
    return overtone1_wave

def second_overtone():
    frequency = 100
    amplitude = 5
    overtone2_wave = amplitude * np.sin(2 * np.pi * frequency * time + 180) 
    return overtone2_wave

composite_signal = fundamental_frequency() + first_overtone() + second_overtone()


plot.figure(figsize=(10, 6))

#FUNDAMENTAL FREQUENCY
plot.subplot(4, 1, 1)
plot.xlim(0,1)#TO set min and max value in x axis
plot.ylim(-20,20)#To set min and max value in y axis
plot.plot(time, fundamental_frequency())
plot.title("Fundamental Frequency(y1 = 15sin(pi75t))")

#FIRST OVERTONE
plot.subplot(4, 1, 2)
plot.xlim(0,1)#TO set min and max value in x axis
plot.ylim(-20,20)#To set min and max value in y axis
plot.plot(time, first_overtone() , color = 'g')
plot.title("First Overtone(y2 = 10sin(pi150t))")

#SECOND OVERTONE
plot.subplot(4, 1, 3)
plot.xlim(0,1)#TO set min and max value in x axis
plot.ylim(-20,20)#To set min and max value in y axis
plot.plot(time, second_overtone(), color = 'b')
plot.title("Second Overtone(y3 = 5sin(pi200t + 180))")

#COMPOSITE SIGNAL
plot.subplot(4, 1, 4)
plot.xlim(0,1)#TO set min and max value in x axis
plot.ylim(-30,30)#To set min and max value in y axis
plot.plot(time, composite_signal, color='r')
plot.title("Composite Signal(y1+y2+y3)")

plot.tight_layout()
plot.show()
