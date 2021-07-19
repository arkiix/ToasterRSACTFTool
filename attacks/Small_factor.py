def attack(n, e, c):
    p = 0
    q = 0

    for factor in range(2, 100000):
        if n % factor == 0:
            p = factor
            q = n // factor
            break
    else:
        return None

    return [p, q]