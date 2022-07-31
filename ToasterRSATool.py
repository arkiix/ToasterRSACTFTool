import Arguments_parser
import config
import models
from RSA import Cipher
from attacks.Attacks import Attacks


def print_pos(text):
    print(text, end=' '*(40 - len(text)))


def print_color(text, color: str):
    color_num = 31 if color.lower() == 'red' else 32
    print(f'\033[{color_num}m{text}\033[0m')


def validate_decrypt_text(decrypt_text):
    if decrypt_text:
        res_datatype = type(decrypt_text)
        if res_datatype is list:
            input_data.p, input_data.q = decrypt_text

        elif res_datatype is int:
            input_data.d = decrypt_text

        if res_datatype not in (str, bytes):
            decrypt_text = Cipher(input_data=input_data).decrypt(input_data.c)

    res = None
    if not decrypt_text:
        print_color('FAIL', 'red')
    else:
        if type(decrypt_text) is bytes:
            try:
                res = decrypt_text.decode()
            except:
                print_color('FAIL', 'red')
    return res


def attack(input_data: models.Input_Data):
    if input_data.d and input_data.n:
        print_pos('RSA decryption...')
        dt = Cipher(input_data=input_data).decrypt(input_data.c)
        res = validate_decrypt_text(dt)

        if res:
            return res

    if input_data.p and input_data.q:
        if not input_data.n:
            input_data.n = input_data.p * input_data.q

        if not input_data.e:
            input_data.e = 65537

        print_pos('RSA decryption...')
        dt = Cipher(input_data=input_data).decrypt(input_data.c)
        res = validate_decrypt_text(dt)

        if res:
            return res

    if input_data.e and input_data.n:
        priority_f = []

        if input_data.e < 1000:
            priority_f.append(Attacks.little_exponent)

        elif input_data.e > 70000:
            priority_f.append(Attacks.wiener)

        if (input_data.p and not input_data.q) or (not input_data.p and input_data.q):
            priority_f.append(Attacks.one_factor)

        if input_data.n2:
            priority_f.append(Attacks.gcd)

        attack_functions = list(filter(lambda x: not x[0].startswith('_'), Attacks.__dict__.items()))

        # Сортировка атак по приоритету
        attack_functions.sort(key=lambda x: 0 if x[1] in priority_f else 1)

        for name, func in attack_functions:
            print_pos(f'Start {name} attack...')
            res = func(input_data)

            res = validate_decrypt_text(res)
            if res:
                return res


if __name__ == '__main__':
    print('\033[33m{}\033[0m'.format(config.HEAD))

    input_data = Arguments_parser.parse()

    if input_data.encrypt:
        cipher = None
        if not input_data.key:
            cipher = Cipher()
            public_key = cipher.key.publickey().exportKey()
            private_key = cipher.key.exportKey()

            with open('keys/pub.pem', 'w') as f:
                f.write(public_key.decode())

            with open('keys/private.pem', 'w') as f:
                f.write(private_key.decode())

        else:
            cipher = Cipher(key=input_data.key)

        c = hex(cipher.encrypt(input_data.encrypt))

        print(f'{c = }')
        print_color('Keys are automatically saved in /keys\n', 'green')

    else:
        if input_data.key:
            key = Cipher(input_data.key).key

            input_data.n = key.n if not input_data.n else input_data.n
            input_data.e = key.e if not input_data.e else input_data.e
            try:
                input_data.d = key.d if not input_data.d else input_data.d
                input_data.p = key.p if not input_data.p else input_data.p
                input_data.q = key.q if not input_data.q else input_data.q
            except:
                pass

        if input_data.c:
            answer = attack(input_data)

            if not answer:
                print_color('None ;(', 'red')
            else:
                print_color(answer, 'green')
        else:
            print_color('No ciphertext [-c]', 'red')
