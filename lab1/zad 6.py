# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami np. "la la la".
# Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa "la".

# tekst piosenki "Naughty Boy - La la la ft. Sam Smith"
lyrics = """La la, la la la la la na na na na na
La la na na, la la la la la na na na na na
La la, la la la la la na na na na na
La la na na, la la la la la na na na na na
"""

print(lyrics.lower().count('la'))
