import numpy as np


def generate_power_array(n, a):
    return np.logspace(1, a, base=n, num=a, dtype='int')


print(generate_power_array(2, 4))
print(generate_power_array(2, 10))
