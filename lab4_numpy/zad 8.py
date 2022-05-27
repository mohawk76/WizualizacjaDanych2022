import numpy as np


def divide_array(arr, direction):
    if direction == "h":
        if arr.shape[1] % 2 != 0:
            print('Ilość kolumn nie pozwala na wykonanie operacji!')
            return
        return np.hsplit(arr, 2)
    elif direction == "v":
        if arr.shape[0] % 2 != 0:
            print('Ilość wierszy nie pozwala na wykonanie operacji!')
            return
        return np.vsplit(arr, 2)
    else:
        raise Exception("Unknown separation direction")


a = np.arange(12).reshape((4, 3))
print(divide_array(a, "h"))
print(divide_array(a, "v"))
