"""
WRITE ME
"""
from blit import Blit
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import wavio


def sythesize(rate, f, pw):
    """
    Sytheszie a square/pulse wave a a trianlgle/saw

    args:
        rate - audio sample rate
        f - numpy array of frequecne at each step
        pw - numpy array of pulsewidth at each step

    return:
        pair of numpy arrays (square/pulse, triangle/saw)
    """
    N = len(f)

    # Set up band limited impulse train class
    blit = Blit(rate, 256) # work with interpolation

    # Holds the calculated pulse train
    x = np.linspace(0, 0, N)
    # Holds the lossy integral of x, i.e. the resulting pulse wave
    y = np.linspace(0, 0, N)
    # Holds the lossy integral of y, i.e. the resulting triangle
    z = np.linspace(0, 0, N)

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
        R=0.9995
        # Integrate once for square wave
        y[i] = x[i] - x[i-1] + 2* R * y[i-1] - R*R*(y[i-2] if i>=2 else 0)
        # Integrate again for tri
        z[i] = f[i]*(y[i] - y[i-1]) + 2*R* z[i-1] - R*R*(z[i-2] if i>=2 else 0)

    return y, z
