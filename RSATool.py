import Arguments_parser, RSA
from attacks import FactorDB_attack, Gcd, Little_exponent, Wiener_attack, One_factor, Square, Monoprime

head = '''
 _   _            _   ______  _____  ___ _____           _ 
| | | |          | |  | ___ \/  ___|/ _ \_   _|         | |
| |_| | __ _  ___| | _| |_/ /\ `--./ /_\ \| | ___   ___ | |
|  _  |/ _` |/ __| |/ /    /  `--. \  _  || |/ _ \ / _ \| |
| | | | (_| | (__|   <| |\ \ /\__/ / | | || | (_) | (_) | |
\_| |_/\__,_|\___|_|\_\_| \_|\____/\_| |_/\_/\___/ \___/|_|
                                            Tool by @arkiix                                                           
                                                           
'''

def import_key(key):
    n, e, d = None, None, None

    key = RSA.import_key(key)
    try:
        n = key.n
        e = key.e
        d = key.d
    except:
        if n != key.n or e != key.e:
            print('Error import key!')

    return n, e, d


def attack(n, p, q, e, d, c, n2):
    if d != None and n != None:
        dt = RSA.decrypt(c, n, d)
        try:
            return dt.decode()
        except:
            pass

    if p != None and q != None:
        if n == None:
            n = p * q

        if e == None:
            e = 65537

        d = RSA.private_exponent(p, q, e)
        dt = RSA.decrypt(c, n, d)
        try:
            return dt.decode()
        except:
            pass

    if e != None and n != None:
        if e < 1000:
            dt = Little_exponent.attack(n, e, c)
            try:
                return dt.decode()
            except:
                pass

        factor = None
        if p != None and q == None:
            factor = p
        elif p == None and q != None:
            factor = q
        dt = One_factor.attack(n, e, factor, c)
        try:
            return dt.decode()
        except:
            pass


        if n2 != None:
            dt = Gcd.attack(n, e, n2, c)

            if dt != None:
                try:
                    return dt.decode()
                except:
                    pass


        fast_attack = [FactorDB_attack.attack, Wiener_attack.attack, Square.attack, Monoprime.attack]

        for i in fast_attack:
            dt = i(n, e, c)

            if dt != None:
                try:
                    return dt.decode()
                except:
                    continue

print(head)

n, p, q, e, d, c, n2, key, enc = Arguments_parser.parse()

if enc != None:
    public_key = None
    private_key = None

    if key == None:
        key = RSA.generate_key()
        public_key = key.publickey().exportKey()
        private_key = key.exportKey()
    else:
        n, e, d = import_key(key)

    c = RSA.encrypt(enc, n, e)

    if public_key != None:
        print(public_key.decode() + '\n')
        print(private_key.decode() + '\n')
        print(f'{n = }\n{e = }\n{d = }\n')
    print(f'{c = }')
else:
    if key != None:
        n, e, d = import_key(key)

    if c != None:
        answer = str(attack(n, p, q, e, d, c, n2))
        if answer == None:
            answer += ' ;('
        print(answer)
    else:
        print('No ciphertext [-c]')