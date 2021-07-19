from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA
from base64 import b64decode

def generate_key():
    return RSA.generate(2048)

def encrypt(plain, n, e):

    c = pow(bytes_to_long(plain.encode()), e, n)

    return c

def private_exponent(p, q, e):
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return d

def import_key(path):
    try:
        with open(path, "rb") as k:
            key = RSA.importKey(k.read())
    except:
        return None
    return key

def decrypt(cipher, n, d):
    dt = pow(cipher, d, n)
    return long_to_bytes(dt)