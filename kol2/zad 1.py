import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 1)
plt.plot(x, (x ** 3) + 2 * (x ** 2), label='f(x) = x^3 + 2x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim([-5, 5])
plt.title('Wykres funkcji f(x) = x^3 + 2x^2 dla x[-5, 5]')
plt.show()
