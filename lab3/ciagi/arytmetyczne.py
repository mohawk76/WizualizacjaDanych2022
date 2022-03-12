def nth_elem(n, n0=0, step=1):
    val = n0
    for x in range(0, n):
        val += step
    return val
