from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

def attack(n, e, c):
    while True:
        root = iroot(c, e)
        if root[1] == True:
            return long_to_bytes(root[0])
        else:
            c += n