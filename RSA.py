from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.PublicKey import RSA
import models


class Cipher:
    def __init__(self, key: bytes = None, input_data: models.Input_Data = None):
        if key:
            self.key = RSA.importKey(open(key, 'r').read())
        elif input_data:
            self.key = input_data
        else:
            self.key = self.generate_key()

    @staticmethod
    def generate_key():
        return RSA.generate(2048)

    def encrypt(self, plain):
        c = pow(bytes_to_long(plain.encode()), self.key.e, self.key.n)
        return c

    def calculate_private_exponent(self):
        if not (self.key.p and self.key.q and self.key.e):
            return None

        phi = (self.key.p - 1) * (self.key.q - 1)
        d = pow(self.key.e, -1, phi)
        return d

    def decrypt(self, cipher):
        d = self.key.d

        if not d:
            d = self.calculate_private_exponent()

        dt = pow(cipher, d, self.key.n)
        return long_to_bytes(dt)
