import numpy as np

a = np.arange(5, dtype='float', step=0.5)
print('Wersja z wartościami typu float:')
print(a)
b = a.astype('int64')
print('Wersja z wartościami typu int64:')
print(b)
