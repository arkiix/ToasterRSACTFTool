from Crypto.Util.number import long_to_bytes
import owiener

def attack(n, e, c):
    d = owiener.attack(e, n)

    if d == None:
        return None

    dt = pow(c, d, n)

    return long_to_bytes(dt)