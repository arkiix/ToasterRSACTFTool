from math import isqrt
from Crypto.Util.number import long_to_bytes

def attack(n, e, c):
    f = isqrt(n)

    if f * f != n:
        return None

    phi = f * (f - 1)

    d = pow(e, -1, phi)
    dt = pow(c, d, n)

    return long_to_bytes(dt)