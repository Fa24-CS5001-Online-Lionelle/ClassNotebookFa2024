import sys
import random

ENCRYPT = "encrypt"
DECRYPT = "decrypt"



def caesar_cipher(message, key):
   msg = ''
   for character in message:
       numeric = ord(character)
       shifted = numeric + key
       new_char = chr(shifted)
       msg += new_char


   return msg 


def encrypt(message, key):
    return caesar_cipher(message, key)


def decrypt(message, key):
    return caesar_cipher(message, -1 * key)


def print_encrypted(message, key):
    print(f"Message={message}\nkey={key}")

def print_decrypted(message):
    print(f"Message={message}")

def main(_action, _msg, _key):
    if _action == ENCRYPT:
        if not _key:
            _key = random.randint(1, 26)
        else:
            _key = int(_key)
        encrypted_message = encrypt(_msg, _key)
        print_encrypted(encrypted_message, _key)
    else: 
        if not _key: 
            return
        _key = int(_key)
        decryted_message = decrypt(_msg, _key)
        print_decrypted(decryted_message)


    



if __name__ == "__main__":
        # check to see if there are command line arguments
    _action = 'encrypt'
    _msg = ''
    _key = ''
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            _action = 'decrypt'
            remainder = sys.argv[2:]
        else:
            remainder = sys.argv[1:]
        if len(remainder) > 0:
            _msg = remainder[0]
            if len(remainder) > 1:
                _key = remainder[1]
    main(_action, _msg, _key)


