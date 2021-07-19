from Crypto.Util.number import long_to_bytes
from factordb.factordb import FactorDB

def attack(n, e, c):
    f = FactorDB(n)
    f.connect()
    factors = f.get_factor_list()

    if len(factors) == 1:
        return None

    phi = 1
    for i in factors:
        phi *= i - 1

    d = pow(e, -1, phi)
    dt = pow(c, d, n)

    return long_to_bytes(dt)