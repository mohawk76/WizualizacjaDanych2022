def products_stat(**products):
    value = sum(products.values())
    counter = len(products.keys())
    return {"ilość": counter, "wartość": value}


print(products_stat(mleko=2.65, masło=5.25, ziemniaki=3.65))