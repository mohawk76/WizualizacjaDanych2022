import numpy as np

arr = np.random.randint(1, 100, 81).reshape((9, 9))
print(arr)
print(arr.reshape((27,3)))
print(arr.reshape((81,1)))