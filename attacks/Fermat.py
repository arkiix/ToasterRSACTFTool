from math import isqrt


def attack(n, iterations):
    a = b = isqrt(n)
    b2 = pow(a, 2) - n

    cnt = 0
    while pow(b, 2) != b2 and cnt < iterations:
        a += 1
        b2 = pow(a, 2) - n
        b = isqrt(b2)
        cnt += 1

    p, q = (a + b), (a - b)

    if n != p * q:
        return None

    return [p, q]