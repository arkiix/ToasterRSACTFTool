from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes
import config


def attack(input_data):
    cnt = 0
    while True:
        try:
            root = iroot(input_data.c, input_data.e)
        except:
            root = (0, False)

        if root[1]:
            return long_to_bytes(root[0])
        else:
            input_data.c += input_data.n

        if cnt > config.LITTLE_EXPONENT_ITERATIONS:
            return None
        else:
            cnt += 1