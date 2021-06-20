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

freqeucies = np.logspace(7, 14, resolution, base=2)

fig = plt.figure()
axs = fig.subplots(2, 1)
axs[0].set_title('Square wave max-min')
axs[1].set_title('Tri wave max-min')

for pw in np.linspace(0.5, 0.99, resolution):
    print('pw', pw)
    rng_sqr = np.linspace(0,0,resolution)
    rng_tri = np.linspace(0,0,resolution)
    pulse_width = np.linspace(pw, pw, N)
    for i, f in enumerate(freqeucies):
        print('f', f)
        freq = np.linspace(f, f, N)
        sqr, tri = sythesize(rate, freq, pulse_width)
        # Take only the last second
        rng_sqr[i] = np.max(sqr[-rate:]) - np.min(sqr[-rate:])
        rng_tri[i] = np.max(tri[-rate:]) - np.min(tri[-rate:])

    axs[0].plot(freqeucies, rng_sqr, label=f'pw={pw}')
    axs[1].plot(freqeucies, rng_tri, label=f'pw={pw}')

plt.legend()
plt.show()
