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

def windowed_bl_impulse(fs, over_sampling, crossings):
    """
    Creates a np array for a windowed band-limited impulse function

    args:
        fs - audio sample rate
        over_sampling - factor to oversample this function
        crossings - how many zero crossings should be included in the window (on each side of x=0)

    returns:
        numpy array
    """
    times = np.linspace(-crossings/fs, crossings/fs, 2*crossings*over_sampling)
    window = signal.windows.blackman(2*crossings*over_sampling)
    fn = np.vectorize(lambda t: bl_impulse(fs, t))
    return window * fn(times)

if __name__ == '__main__':
    N = 40000
    x = np.linspace(-60, 60, N)
    y = np.vectorize(sinc)(x)
    bw  = signal.windows.blackman(N)
    plt.plot(x, y)
    plt.plot(x, y*bw)
    plt.show()
    plt.plot(windowed_bl_impulse(44100, 1024, 16))
    plt.show()
