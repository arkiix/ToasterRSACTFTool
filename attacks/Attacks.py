from attacks import FactorDB, Fermat, GCD, Little_exponent, Monoprime, One_factor, Small_factor, Square, Wiener


class Attacks:
    factor_db = FactorDB.attack
    fermat = Fermat.attack
    gcd = GCD.attack
    little_exponent = Little_exponent.attack
    monoprime = Monoprime.attack
    one_factor = One_factor.attack
    small_factor = Small_factor.attack
    square = Square.attack
    wiener = Wiener.attack