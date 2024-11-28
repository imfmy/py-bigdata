import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# 密钥生成
SECRET_KEY = b"1234567812345678"  # 16 字节密钥
IV = b"1234567812345678"         # 初始向量
# 加密函数
def encrypt(plain_text):
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(IV), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted = encryptor.update(plain_text.encode()) + encryptor.finalize()
    return base64.b64encode(encrypted).decode()

# 解密函数
def decrypt(encrypted_text):
    encrypted_text_bytes = base64.b64decode(encrypted_text)
    cipher = Cipher(algorithms.AES(SECRET_KEY), modes.CFB(IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(encrypted_text_bytes) + decryptor.finalize()
    return decrypted.decode()

if __name__ == '__main__':
    print(encrypt('1334343'))
    # ASsg29bVBQ ==
    print(decrypt(encrypt('1334343')))
    print(decrypt("XJ8vYtRzyQ=="))