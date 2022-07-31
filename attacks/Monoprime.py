def attack(input_data):
    phi = input_data.n - 1

    try:
        d = pow(input_data.e, -1, phi)
    except:
        return None

    return d