def get_number_from_user():
    while True:
        user_input = input()
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Podałeś błędną wartość. Wprowadź ponownie liczbę")


number_list = []
iterations = 10

while iterations != 0:
    print("Wprowadź liczbę: ")
    number = get_number_from_user()
    if number % 2 == 0:
        number_list.append(number)
    iterations -= 1

print('Lista liczb parzystych z wprowadzonych liczb: ', number_list)
