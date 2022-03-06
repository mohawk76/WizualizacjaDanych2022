# Napisz pierwszy skrypt,w którym zadeklarujesz po dwie zmienne każdego typu, a następnie wyświetl te zmienne
string_variable = "string"
string_variable2 = "string2"

int_variable = 5
int_variable2 = 6

float_variable = 1.5
float_variable2 = 3.14

complex_variable = 1 + 1j
complex_variable2 = 3 + 1j

print("Pierwszy ciąg znaków: %s" % string_variable)
print("Drugi ciąg znaków: %s" % string_variable2)

print("Pierwsza liczba całkowita: %d" % int_variable)
print("Druga liczba całkowita: %d" % int_variable2)

print("Pierwsza liczba zmiennoprzecinkowa: %f" % float_variable)
print("Druga liczba zmiennoprzecinkowa: %f" % float_variable2)

# Rzutowanie complex na string
print("Pierwsza liczba urojona: %s" % complex_variable)
print("Druga liczba urojona: %s" % complex_variable2)
