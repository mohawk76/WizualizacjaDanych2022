import numpy as np


def generate_array(n):
    size = n * n
    arr = np.arange(size)
    return arr.reshape((n, n))


print(generate_array(5))
