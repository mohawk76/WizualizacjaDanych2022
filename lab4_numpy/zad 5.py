import numpy as np


def generate_vector(length):
    a = np.random.random(length)
    a = np.flip(a)
    return np.diag(a)


print(generate_vector(4))
