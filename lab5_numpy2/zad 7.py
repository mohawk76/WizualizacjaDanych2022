import numpy as np

arr = np.random.randint(1, 100, 6).reshape((2, 3))
a = np.sin(arr)

arr = np.random.randint(1, 100, 6).reshape((2, 3))
b = np.cos(arr)

print(a + b)
