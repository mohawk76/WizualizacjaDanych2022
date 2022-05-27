import numpy as np

def generate_matrix(n):
    arr = np.array([2 for x in range(n * n)]).reshape((n, n))

    for i in range(n):
        for j in range(n):
            multiplier = abs(j-i)+1
            arr[i][j] *= multiplier

    return arr


print(generate_matrix(12))
