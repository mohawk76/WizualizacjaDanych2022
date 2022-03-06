operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


def get_number_from_user():
    while True:
        user_input = input()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Podałeś błędną wartość. Wprowadź ponownie liczbę")


def calculator():
    operation = input("Wybierz operację matematyczną (+, -, *, /) lub wyjdź z programu (q): ")
    if operation == "q":
        return True
    if operation not in operations:
        print("Program nie posiada zdefiniowanej wybranej operacji!")
        return False
    else:
        print("Wprowadź pierwszą wartość")
        a = get_number_from_user()
        print("Wprowadź drugą wartość wartość")
        b = get_number_from_user()
        try:
            print("Wynik działania to: %.4f" % operations.get(operation)(a, b))
        except ZeroDivisionError:
            print("Nie można dzielić przez 0")
    return False


while True:
    if calculator(): break
