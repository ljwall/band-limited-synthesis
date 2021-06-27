"""
WRITE ME
"""
from sythesize import sythesize
import matplotlib.pyplot as plt
import numpy as np
import wavio

# samples per second
rate = 44100

# Oversampling rate for the band limited impulse
omega = 256

# number of crosssing (eash side of the pulse) to take in the band limited impulse
crosssings = 16

# sample duration (seconds)
T = 10

N = T * rate

# freq (Hz)
f = np.linspace(110, 110, N)
#f = np.logspace(5, 13, N, base=2) # 32 to 8192 Hz

pulse_width = 0.5 + 0.4*np.sin(np.linspace(0, 10*np.pi, N))
#pulse_width = np.linspace(0.5, 0.5, N)
#pulse_width = np.linspace(0.5, 0.99, N)

sqr = sythesize(rate, omega, crosssings, f, pulse_width)

plt.plot(sqr)
plt.show()
wavio.write("sqr.wav", 0.2*sqr, rate, sampwidth=4, scale=(-1, 1))
