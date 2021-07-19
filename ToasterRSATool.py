import Arguments_parser, RSA
from attacks import FactorDB_attack, Gcd, Little_exponent, Wiener_attack, One_factor, Square, Monoprime, Small_factor, Fermat

head = '''
  ______                 __            ____  _____ ___  ______            __
 /_  __/___  ____ ______/ /____  _____/ __ \/ ___//   |/_  __/___  ____  / /
  / / / __ \/ __ `/ ___/ __/ _ \/ ___/ /_/ /\__ \/ /| | / / / __ \/ __ \/ / 
 / / / /_/ / /_/ (__  ) /_/  __/ /  / _, _/___/ / ___ |/ / / /_/ / /_/ / /  
/_/  \____/\__,_/____/\__/\___/_/  /_/ |_|/____/_/  |_/_/  \____/\____/_/   
                                                             Tool by @arkiix
'''

def print_pos(text):
    print(text, end=' '*(40 - len(text)))

def print_red(text):
    print("\033[31m{}\033[0m".format(text))

def print_green(text):
    print("\033[32m{}\033[0m" .format(text))

def import_key(key):
    n = e = d = None

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
    def check_result(dt):
        if dt == None:
            print_red('FAIL')
        else:
            try:
                return dt.decode()
            except:
                print_red('FAIL')
        return None

    if d != None and n != None:
        print_pos('RSA decryption...')
        dt = RSA.decrypt(c, n, d)

        res = check_result(dt)
        if res != None:
            return res


    if p != None and q != None:
        if n == None:
            n = p * q

        if e == None:
            e = 65537

        print_pos('Computing a private exponent...')
        d = RSA.private_exponent(p, q, e)
        print_green('SUCCES')
        print_pos('RSA decryption...')
        dt = RSA.decrypt(c, n, d)

        res = check_result(dt)
        if res != None:
            return res

    if e != None and n != None:
        if e < 1000:
            print_pos('Little_exponent.attack...')
            dt = Little_exponent.attack(n, e, c)

            res = check_result(dt)
            if res != None:
                return res

        if (p != None and q == None) or (p == None and q != None):
            if p != None:
                factor = p
            else:
                factor = q
            print_pos('Start One_factor.attack...')
            p, q = One_factor.attack(n, factor)
            d = RSA.private_exponent(p, q, e)
            dt = RSA.decrypt(c, n, d)
            res = check_result(dt)
            if res != None:
                return res


        if n2 != None:
            print_pos('Start Gcd.attack...')
            p, q = Gcd.attack(n, n2)
            d = RSA.private_exponent(p, q, e)
            dt = RSA.decrypt(c, n, d)
            res = check_result(dt)
            if res != None:
                return res


        fast_attack = [FactorDB_attack.attack, Wiener_attack.attack, Square.attack, Monoprime.attack, Small_factor.attack, Fermat.attack]
        fast_attack_str = ['FactorDB.attack', 'Wiener.attack', 'Square.attack', 'Monoprime.attack',
                       'Small_factor.attack', 'Fermat.attack']

        for i, name in zip(fast_attack, fast_attack_str):
            print_pos(name + '...')
            a = i(n, e, c)
            if a != None:
                if type(a) is list:
                    p, q = a
                    d = RSA.private_exponent(p, q, e)
                    a = RSA.decrypt(c, n, d)

            res = check_result(a)
            if res != None:
                return res

print('\033[33m{}\033[0m'.format(head))

n, p, q, e, d, c, n2, key, enc = Arguments_parser.parse()

if enc != None:
    public_key = private_key = None

    if key == None:
        key = RSA.generate_key()
        public_key = key.publickey().exportKey()
        private_key = key.exportKey()
        with open('keys/pub.pem', 'w') as f:
            f.write(public_key.decode())
        with open('keys/private.pem', 'w') as f:
            f.write(private_key.decode())
        n, e, d = key.n, key.e, key.d
    else:
        n, e, d = import_key(key)

    c = RSA.encrypt(enc, n, e)

    if public_key != None:
        print(public_key.decode() + '\n')
        print(private_key.decode() + '\n')
        #print(f'{n = }\n{e = }\n{d = }\n')

    print(f'{c = }')
    print_green('\nKeys are automatically saved in /keys\n')
else:
    if key != None:
        n, e, d = import_key(key)

    if c != None:
        answer = attack(n, p, q, e, d, c, n2)
        if answer == None:
            print_red('None ;(')
        else:
            print_green(answer)
    else:
        print_red('No ciphertext [-c]')