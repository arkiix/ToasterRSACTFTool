# ToasterRSATool

A tool for working with RSA, can encrypt, decrypt, recover the private key by exploiting attacks.

# Usage

> usage: ToasterRSATool.py [-h] [-n N] [-p P] [-q Q] [-e E] [-d D] [-c C] [-n2 N2] [--key KEY] [--encrypt ENCRYPT]

Argument | Description
------------ | -------------
-h, --help | show this help message and exit
-n N | Module n
-p P | Factor p
-q Q | Factor q
-e E | Public exponent
-d D | Private exponent
-c C | Cipher text
-n2 N2 | Second n
--key KEY | Path to the key
--encrypt ENCRYPT | Encrypt message

## Attack/Decrypt RSA

To attack or decrypt RSA, provide all the data you have. The tool will start attacking when you give it data that is not enough to decrypt.

## Encrypt RSA

To encrypt the message, you must use --encrypt "message". Keys are automatically generated and displayed to you, saved in /keys. You can use your own key for encryption, then you need to add --keys path_to_key.

### Encryption using generated keys

    python3 ToasterRSATool.py --encrypt "Your message"
    
### Encryption with your key

    python3 ToasterRSATool.py --key pub.pem --encrypt "Your message"
    
### Decrypt message
    python3 ToasterRSATool.py --key private.pem -c 1234567890
    
    python3 ToasterRSATool.py -n 1234567890 -c 1234567890 -d 1234567890
    
### Examples of starting an attack
    python3 ToasterRSATool.py -n 1234567890 -e 65537 -c 1234567890
    
    python3 ToasterRSATool.py --key public.pem -e 65537 -c 1234567890
    
    python3 ToasterRSATool.py -n 1234567890 -e 65537 -c 1234567890 -n2 1234567890
    
    python3 ToasterRSATool.py -n 1234567890 -e 65537 -c 1234567890 -p 1234567890
    
    python3 ToasterRSATool.py -n 1234567890 -e 65537 -c 1234567890 -q 1234567890
    
## Installation
### Requirements
* pycryptodome
* factordb-pycli
* gmpy2
* owiener

### Ubuntu and Kali specific Instructions
    git clone https://github.com/arkiix/ToasterRSACTFTool
    cd ToasterRSACTFTool
    pip3 install -r requirements.txt
    python3 ToasterRSATool.py
    
### MacOS-specific Instructions
If you cannot install using this command:
    
    pip3 install -r requirements.txt
It might work, it: 

    easy_install `cat requirements.txt`
