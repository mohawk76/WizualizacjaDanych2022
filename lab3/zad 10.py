with open('zad 10.txt', 'w') as file:
    file.write("\n".join([str(x) for x in range(0, 101) if x % 4 == 0]))

print("Został wygenerowany plik 'zad 10.txt' z liczbami podzielnymi przez 4")
