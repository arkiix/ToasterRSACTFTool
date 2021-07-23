from math import gcd


def attack(n, f):
    p = gcd(n, f)
    q = n // p

    if p == 1 or p * q != n:
        return None
    
    return [p, q]