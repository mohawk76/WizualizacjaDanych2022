import numpy as np

def display(flat):
    for x in flat:
        print(x, end=" ")
    print()

arr = np.random.randint(1, 100, 12)
a = arr.reshape((3,4))
b = arr.reshape((4,3))
c = arr.reshape((2,6))

display(a.flat)
display(b.flat)
display(c.flat)