"""
Produce some plots of the sinc function: using sin(x)/x away from zero and
taylor expansion over zero
"""
import matplotlib.pyplot as plt
import math
import numpy as np


if __name__ == '__main__':
    x = np.linspace(-5, 5, 500)
    y1 = np.sin(x)
    y2 = x - x**3 / math.factorial(3) + x**5 / math.factorial(5) - x**7 / math.factorial(7) + x**9 / math.factorial(9)

    y3 = 1 - x**2 / math.factorial(3) + x**4 / math.factorial(5) - x**6 / math.factorial(7) + x**8 / math.factorial(9)

    xplus = np.linspace(0.1, 40, 2000)
    sinc = np.sin(xplus)/xplus

    plt.figure(num = 3, figsize=(8, 5))
    # plt.plot(x, y2)
    # plt.plot(x, y1,
    #     color='red',
    #     linewidth=1.0,
    #     linestyle='--'
    # )
    plt.plot(x, y3)
    plt.plot(xplus, sinc)

    plt.show()
