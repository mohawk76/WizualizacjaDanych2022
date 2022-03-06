# Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery "a".
# Użyj funkcji input.

user_input = input("Wpisz zdanie, a ja zliczę ile razy w nim występuje litera 'a':\n")
print(user_input.lower().count('a'))
