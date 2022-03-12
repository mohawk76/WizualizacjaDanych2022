products1 = {
    "mleko": "l",
    "jajka": "szt",
    "ziemniaki": "kg",
    "awokado": "szt",
}

print("Pierwsza lista produktów: ", products1)

products2 = {k: v for (k, v) in products1.items() if v == "szt"}

print("Druga lista produktów, których jednostka to sztuki: ", products2)
