"""
WRITE ME
"""
from sythesize import sythesize
import matplotlib.pyplot as plt
import numpy as np
import math

# samples per second
rate = 44100

# sample duration (seconds)
T = 3

N = T * rate

resolution = 10

plt.suptitle('Tri wave max-min')

rng_tri = np.linspace(0,0,resolution)
freq = np.linspace(220, 220, N)
pws = np.linspace(0.5, 0.99, resolution)

for i, pw in enumerate(pws):
    pulse_width = np.linspace(pw, pw, N)
    _, tri = sythesize(rate, freq, pulse_width)
    # Take only the last second
    rng_tri[i] = np.max(tri[-rate:]) - np.min(tri[-rate:])

plt.plot(pws, rng_tri)
plt.show()
