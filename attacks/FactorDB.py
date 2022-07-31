from factordb.factordb import FactorDB


def attack(input_data):
    f = FactorDB(input_data.n)

    try:
        f.connect()
    except:
        return None

    factors = f.get_factor_list()

    if len(factors) == 1:
        return None

    phi = 1
    for i in factors:
        phi *= i - 1

    d = pow(input_data.e, -1, phi)

    return d