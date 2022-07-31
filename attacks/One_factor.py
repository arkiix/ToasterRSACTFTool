def attack(input_data):
    if not (input_data.p or input_data.q):
        return None

    p = input_data.p if input_data.p else input_data.q

    q = input_data.n // p

    if p * q != input_data.n:
        return None

    return [p, q]