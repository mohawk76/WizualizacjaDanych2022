import numpy as np

fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
fib_arr = np.array([fib(x) for x in range(5 * 5)]).reshape((5, 5))
print(fib_arr)
