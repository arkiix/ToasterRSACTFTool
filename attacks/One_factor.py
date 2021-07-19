def attack(n, f):
    p = f
    q = n // p

    if p * q != n:
        return None

    return [p, q]