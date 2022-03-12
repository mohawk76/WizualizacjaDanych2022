def product_sequence(*params):
    params_length = len(params)
    if params_length == 3:
        (a, b, c) = params
    elif params_length == 2:
        (a, b) = params
        c = 10
    elif params_length == 1:
        (a) = params
        b = 4
        c = 10
    else:
        a = 1
        b = 4
        c = 10

    result = [a]
    for x in range(1, c):
        result.append(result[x - 1] * b)
    return result


print(product_sequence())
print(product_sequence(2, 2, 10))
print(product_sequence(2, 4, 10))
