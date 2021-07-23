from Crypto.Util.number import long_to_bytes


def attack(n, e, c):
    phi = n - 1

    try:
        d = pow(e, -1, phi)
    except:
        return None

    dt = pow(c, d, n)
    return long_to_bytes(dt)