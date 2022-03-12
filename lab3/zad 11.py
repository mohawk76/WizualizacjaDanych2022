try:
    with open("zad 10.txt", 'r') as file:
        print("##### Początek zawartości pliku zad 10.txt ####")
        for line in file:
            print(line, end='')
        print("\n##### Koniec zawartości pliku zad 10.txt ####")
except FileNotFoundError:
    print("Nie znaleziono pliku 'zad 10.txt'")
