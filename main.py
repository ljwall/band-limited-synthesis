from sinc import bl_impulse

from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
import wavio

# samples per second
rate = 44100

# sample duration (seconds)
T = 0.2

# freq (Hz)
f = 1500

i = np.vectorize(lambda t: bl_impulse(rate, t))

def impulse_at(t):
    times = np.linspace(0, T, T*rate, endpoint=False)
    return i(times - t)

if __name__ == '__main__':
    step = 0.5/f
    up = True
    t = 0
    impulse_train = np.linspace(0, 0, T*rate)

    while t < T:
        if up:
            impulse_train = impulse_train + impulse_at(t)
        else:
            impulse_train = impulse_train - impulse_at(t)
        up = not up
        t = t + step

    y = signal.lfilter([1], [1, -0.99], impulse_train)
    #y = integrate.cumtrapz(impulse_train, dx=1, initial=0)
    wavio.write("sqr_bl.wav", 0.06*y, rate, sampwidth=4, scale=(-1, 1))
    plt.plot(y)

    plt.show()
