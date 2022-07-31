from math import gcd


def attack(input_data):
    if not (input_data.n and input_data.n2):
        return None

    p = gcd(input_data.n, input_data.n2)
    q = input_data.n // p

    if p == 1 or p * q != input_data.n:
        return None
    
    return [p, q]