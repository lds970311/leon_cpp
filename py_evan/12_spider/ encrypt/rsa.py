# coding:utf-8
# time: 2023/6/17
# author: evan
import base64

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher
from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey


def gen_keys():
    random_generator = Random.new().read
    rsa = RSA.generate(2048, random_generator)
    private_key = rsa.export_key()
    public_key = rsa.public_key().export_key()

    with open('rsa_private_key.pom', 'wb') as f:
        f.write(private_key)

    with open('rsa_public_key.pom', 'wb') as f:
        f.write(public_key)


def get_key(key_path) -> RsaKey:
    with open(key_path, 'r') as f:
        content = f.read()
        key = RSA.import_key(content)

    return key


def encrypt(plain_text, public_key):
    plaintext = plain_text.encode()
    cipher = PKCS1_cipher.new(public_key)
    ciphertext = cipher.encrypt(plaintext)
    ciphertext = base64.b64encode(ciphertext).decode()
    return ciphertext


def decrypt(cipher_text, private_key):
    cipher = PKCS1_cipher.new(private_key)
    cipher_text = base64.b64decode(cipher_text)
    plain_text = cipher.decrypt(cipher_text, 0).decode()
    return plain_text


if __name__ == '__main__':
    # gen_keys()
    private_key = get_key('rsa_private_key.pom')
    public_key = get_key('rsa_public_key.pom')
    plain_text = 'leon'
    cipher_text = encrypt(plain_text, public_key)
    print(cipher_text)
    text = decrypt(cipher_text, private_key)
    print(text)
