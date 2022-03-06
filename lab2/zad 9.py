import math


def get_number_from_user():
    while True:
        user_input = input()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Podałeś błędną wartość. Wprowadź ponownie liczbę")


print("Wprowadź liczbę którą chcesz pierwiastkować:")
a = get_number_from_user()
try:
    print("Wynik pierwiastkowania: %f" % math.sqrt(a))
except ValueError:
    print("Podałeś liczbę, z której nie można wyciągnąć pierwiastka")
