"""
WRITE ME
"""
from blit import Blit
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import wavio


def sythesize(rate, omega, crossings, f, pw):
    """
    Sytheszie a square/pulse wave a a trianlgle/saw

    args:
        rate - audio sample rate
        omega - oversampling multiplier of the band limited impulse
        crossings - number of crosssing (eash side of the pulse) to consider
        f - numpy array of frequecne at each step
        pw - numpy array of pulsewidth at each step

    return:
        pair of numpy arrays (square/pulse, triangle/saw)
    """
    N = len(f)

    # Set up band limited impulse train class
    blit = Blit(rate, omega, crossings) # work with interpolation

    # Holds the calculated pulse train
    x = np.linspace(0, 0, N)
    # Holds the lossy integral of x, i.e. the resulting pulse wave
    y = np.linspace(0, 0, N)

    # Running calulation of the aliasing saw
    saw = 0
    high = False

    for i in range(1, N):
        step = f[i]/rate
        if saw + step > pw[i] and not high:
            # time to go high
            blit.add_time((saw + step - pw[i])/step, 1)
            high = True

        saw = (saw + f[i]/rate) % 1

        if saw<pw[i] and high:
            # time to go low
            blit.add_time(saw/step, -1)
            high = False

        x[i] = blit.next()
        R=0.9997
        # Integrate once for square wave
        y[i] = x[i] + R * y[i-1]

    return y
