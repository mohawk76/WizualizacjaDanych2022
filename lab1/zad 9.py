# Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szesnastkowe. Następnie wyświetl je wykorzystując
# odpowiednie formatowanie

name = "Michał"
pi = 3.14159265359
hex_number = 0x22

print("Nazywam sie %s" % name)
print("Liczba pi to w przybliżeniu %.2f" % pi)
print("%d to %s w systemie szesnastkowym" % (hex_number, hex(hex_number)))
