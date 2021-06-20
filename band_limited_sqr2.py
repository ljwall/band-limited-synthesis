"""
WRITE ME
"""
from sythesize import sythesize
import matplotlib.pyplot as plt
import numpy as np
import wavio

# samples per second
rate = 44100

# sample duration (seconds)
T = 10

N = T * rate

# freq (Hz)
f = np.linspace(110, 110, N)
#f = np.logspace(5, 13, N, base=2) # 32 to 8192 Hz

pulse_width = 0.5 + 0.4*np.sin(np.linspace(0, 10*np.pi, N))
#pulse_width = np.linspace(0.5, 0.5, N)
#pulse_width = np.linspace(0.5, 0.99, N)

sqr, tri = sythesize(rate, f, pulse_width)

plt.plot(0.2*sqr)
plt.plot(0.00005*tri)
plt.show()
wavio.write("sqr_bl_2.wav", 0.2*sqr, rate, sampwidth=4, scale=(-1, 1))
wavio.write("tri_bl.wav", 0.00005*tri, rate, sampwidth=4, scale=(-1, 1))
