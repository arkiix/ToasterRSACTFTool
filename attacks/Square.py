from math import isqrt


def attack(input_data):
    f = isqrt(input_data.n)

    if f * f != input_data.n:
        return None

    phi = f * (f - 1)
    d = pow(input_data.e, -1, phi)
    return d