from argparse import ArgumentParser


def parse_number(num_list):
    methods = ['int(num)', 'int(num, 16)', 'int(num[2:], 16)']
    res = []

    for num in num_list:
        number = None
        for i in methods:
            try:
                number = eval(i)
                break
            except:
                continue
        res.append(number)

    return res


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

    return parse_number([args.n, args.p, args.q, args.e, args.d, args.c, args.n2]) + [args.key, args.encrypt]