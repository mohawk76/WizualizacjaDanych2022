from random import randint as random

lista1 = [random(1, 100) for i in range(0, 10)]
print("Lista pierwsza: ", lista1)
lista2 = [x for x in lista1 if x % 2 == 0]
print("Lista druga: ", lista2)
