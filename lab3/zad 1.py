A = [1 - x for x in range(1, 11, 1)]
print("A: ", A)
B = [4 ** x for x in range(1, 8, 1)]
print("B: ", B)
C = [x for x in B if x % 2 == 0]
print("C: ", C)
