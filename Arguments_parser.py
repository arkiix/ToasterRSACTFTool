import string
from argparse import ArgumentParser
import models


def parse_number(num: str):
    if num and num.startswith('0x'):
        return int(num, 16)

    try:
        for symbol in num:
            if symbol not in string.digits:
                num = int(num, 16)
                break
        else:
            num = int(num)
    except:
        pass

    return num


def parse():
    parser = ArgumentParser(description='description!')

    parser.add_argument('-n', help='Module n')
    parser.add_argument('-p', help='Factor p')
    parser.add_argument('-q', help='Factor q')
    parser.add_argument('-e', help='Public exponent')
    parser.add_argument('-d', help='Private exponent')
    parser.add_argument('-c', help='Cipher text')
    parser.add_argument('-n2', help='Second n')
    parser.add_argument('--key', help='Path to the key')
    parser.add_argument('--encrypt', help='Encrypt message')
    args = parser.parse_args()

    return models.Input_Data(**{k: parse_number(v) for k, v in args.__dict__.items()})