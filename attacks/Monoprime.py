from Crypto.Util.number import long_to_bytes

def attack(n, e, c):

    phi = n - 1
    d = pow(e, -1, phi)
    dt = pow(c, d, n)

    return long_to_bytes(dt)