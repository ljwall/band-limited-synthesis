"""
Produce some plots of the sinc function: using sin(x)/x away from zero and
taylor expansion over zero
"""
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import signal

def sinc(x):
    """
    Calculate sin(x)/x
    """
    if abs(x) < 0.1:
        return 1 - x**2 / 6 + x**4 / 120
    return math.sin(x)/x

def bl_impulse(fs, t):
    """
    Impluse function

    i(t) = 1 | t = 0
           0 | otherwise

    except band limited to sample rate (fs) / 2.

    args:
        fs  - sample rate in hz
        t   - value

    return number
    """
    return sinc(np.pi * fs * t)

if __name__ == '__main__':
    N = 40000
    x = np.linspace(-60, 60, N)
    y = np.vectorize(sinc)(x)
    bw  = signal.windows.blackman(N)
    plt.plot(x, y)
    plt.plot(x, y*bw)
    plt.show()
