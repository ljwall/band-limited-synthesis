"""
WRITE ME
"""
from sinc import windowed_bl_impulse

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import wavio

class Blit:
    def __init__(self, fs, omega):
        """
        fs - audio sample rate
        omega - over sampling rate for the band limted impulse
        """
        self.omega = omega
        self.fs = fs
        self.times = []
        self.impulse = windowed_bl_impulse(fs, omega, 32)
        self.len = len(self.impulse)

    def add_time(self, t, value=1):
        """
        t - staring time through the impulse, expressed as a fraction of
            of a time step or the audio sample rate
        value - value of the pulse
        """
        self.times.append((t * self.omega, value))

    def next(self):
        # Add the current state of the all the band limet pulses we have
        result  = sum([v * self.impulse[int(t)] for t, v in self.times])
        # and update the times ready for next time
        self.times = [
            (t + self.omega, v)
            for t, v
            in self.times
            if t+self.omega < self.len
        ]

        return result


# samples per second
rate = 44100

# sample duration (seconds)
T = 25

N = T * rate

# freq (Hz)
#f = np.linspace(440, 440, N)
f = np.logspace(7, 13, N, base=2) # 128 to 8192 Hz (6 Octaves)

pulse_width = np.linspace(0.85, 0.85, N)

# Set up band limited impulse train class
blit = Blit(rate, 1024)

# Holds the calculated pulse train
x = np.linspace(0, 0, N)
# Holds the lossy integral of x, i.e. the resulting squarewave
y = np.linspace(0, 0, N)

# Running calulation of the aliasing triangle
tri = 0
high = False

for i in range(1, N):
    tri = (tri + f[i]/rate) % 1
    if tri>pulse_width[i] and not high:
        # time to go high
        blit.add_time((tri - pulse_width[i])*rate/f[i], 1)
        high = True
    elif tri<pulse_width[i] and high:
        # time to go low
        blit.add_time(tri*rate/f[i], -1)
        high = False

    x[i] = blit.next()
    y[i] = 0.9995*y[i-1] + x[i]

plt.plot(y)
plt.show()
wavio.write("sqr_bl_2.wav", 0.2*x, rate, sampwidth=4, scale=(-1, 1))
