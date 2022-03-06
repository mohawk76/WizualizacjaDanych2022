# Napisz skrypt gdzie pobierasz trzy liczby całkowite, gdzie wykonasz obliczenia a^b + c.
# Użyj instrukcji readline i write

import sys


def get_number_from_user():
    while True:
        user_input = sys.stdin.readline()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Podałeś błędną wartość. Wprowadź ponownie liczbę")


sys.stdout.write("Wprowadź liczbę a: ")
a = get_number_from_user()
sys.stdout.write("Wprowadź liczbę b: ")
b = get_number_from_user()
sys.stdout.write("Wprowadź liczbę c: ")
c = get_number_from_user()
sys.stdout.write("a^b + c = %.4f" % ((a ** b) + c))
