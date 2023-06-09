# coding:utf-8
# time: 2023/6/8
# author: evan


# 把明文拆分成 128bits 的部分，如果最后的部分不足 128bits，就需要进行 padding
# 密钥的长度 128bits，192bits，256bits
# 长度不固定
# CBC 是最常用的模式，还需要一个 128bits 的 iv

import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt(plaintext, key, iv):
    plaintext = plaintext.encode()
    key = key.encode()
    iv = iv.encode()

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    ciphertext = base64.b64encode(ciphertext).decode()
    return ciphertext


def decrypt(ciphertext, key, iv):
    ciphertext = base64.b64decode(ciphertext)
    key = key.encode()
    iv = iv.encode()

    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    plaintext = plaintext.decode()
    return plaintext


plaintext = "apple"
key = "0123456789abcdef"
iv = "abcdef0123456789"

ciphertext = encrypt(plaintext, key, iv)
print(ciphertext)
plaintext = decrypt(ciphertext, key, iv)
print(plaintext)
