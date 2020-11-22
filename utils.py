def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def broken_fact(n):
    return 0 if n == 0 else fact(n)
