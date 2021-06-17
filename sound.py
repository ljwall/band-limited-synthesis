"""
Write some `wav` files.

- a sine wave going from 2^8 Hz up to 2^12 Hz over 10s
- a square wave going from 2^8 Hz up to 2^12 Hz over 10s

play with `ffplay` and the while the sine is smooth the aliasing
is exemely audible and visible on the square wave.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import wavio

# samples per second
rate = 44100

# sample duration (seconds)
T = 10

# timesteps
t = np.linspace(0, T, T*rate, endpoint=False)

# sound frequency (Hz), may be time variying
#f = np.linspace(440.0, 440.0, T*rate)
f = np.logspace(8, 12, T*rate, base=2)

phase = 2*np.pi * integrate.cumtrapz(f, t, initial=0)

x = np.sin(phase) * 0.25
sqr = 0.06 * np.vectorize(lambda x: 1 if x >= 0 else -1)(x)

wavio.write("sqr.wav", sqr, rate, sampwidth=4, scale=(-1, 1))
wavio.write("sine.wav", x, rate, sampwidth=4, scale=(-1, 1))

plt.plot(sqr[:600])
plt.plot(x[:600])
plt.show()
