from Crypto.Util.number import long_to_bytes

def attack(n, e, f, c):
    p = f
    q = n // p

    if p * q != n:
        return None

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    dt = pow(c, d, n)

    return long_to_bytes(dt)