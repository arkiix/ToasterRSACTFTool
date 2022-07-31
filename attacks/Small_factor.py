def attack(input_data):
    for factor in range(2, 100000):
        if input_data.n % factor == 0:
            p = factor
            q = input_data.n // factor
            break
    else:
        return None

    return [p, q]