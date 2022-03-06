# Wczytaj trzy liczby całkowite a, b, c i sprawdź, która z nich jest największa. W zależności od wyniku wyświetl
# odpowiedni komunikat. Użyj zagnieżdżeń.

def get_number_from_user():
    while True:
        user_input = input()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Podałeś błędną wartość. Wprowadź ponownie liczbę")


print("Wprowadź liczbę a: ")
a = get_number_from_user()
print("Wprowadź liczbę b: ")
b = get_number_from_user()
print("Wprowadź liczbę c: ")
c = get_number_from_user()

if a == b and b == c:
    print('Wszystkie liczby są równe')
elif a >= b:
    if a > c:
        print('Liczba a jest największa')
    else:
        print('Liczba c jest największa')
elif b > a:
    if b > c:
        print('Liczba b jest największa')
    else:
        print('Liczba c jest największa')
