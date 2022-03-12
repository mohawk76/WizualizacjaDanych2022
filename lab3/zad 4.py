def is_right_triangle(a, b, c):
    return (a ** 2 + b ** 2) == (c ** 2)


def get_number_from_user():
    while True:
        user_input = input()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Podałeś błędną wartość. Wprowadź ponownie liczbę")


print("Wprowadź długość pierwszej przyprostokątnej:")
a = get_number_from_user()

print("Wprowadź długość drugiej przyprostokątnej:")
b = get_number_from_user()

print("Wprowadź długość przeciwprostokątnej:")
c = get_number_from_user()

if is_right_triangle(a, b, c):
    print("Trójkąt jest prostokątny")
else:
    print("Trójkąt nie jest prostokątny")