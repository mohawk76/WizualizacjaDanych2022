import numpy as np

a = np.random.randint(1, 100, 9).reshape((3, 3))
b = np.random.randint(1, 100, 16).reshape((4, 4))

print(a.min(axis=0))
print(a.min(axis=1))

print(b.min(axis=0))
print(b.min(axis=1))
