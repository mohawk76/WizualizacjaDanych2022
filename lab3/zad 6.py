def product_sequence(a=1, b=4, c=10):
    result = [a]
    for x in range(1, c):
        result.append(result[x - 1] * b)
    return result


print(product_sequence())
print(product_sequence(2, 2, 10))
print(product_sequence(2, 4, 10))
