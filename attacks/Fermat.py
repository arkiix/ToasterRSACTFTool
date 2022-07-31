from math import isqrt
import config


def attack(input_data):
    a = b = isqrt(input_data.n)
    b2 = pow(a, 2) - input_data.n

    cnt = 0
    while pow(b, 2) != b2 and cnt < config.FERMAT_ITERATIONS:
        a += 1
        b2 = pow(a, 2) - input_data.n
        b = isqrt(b2)
        cnt += 1

    p, q = (a + b), (a - b)

    if input_data.n != p * q:
        return None

    phi = (p - 1) * (q - 1)
    d = pow(input_data.e, -1, phi)
    return d