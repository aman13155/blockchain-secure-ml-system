import hashlib
from Crypto.Cipher import AES, DES, Blowfish, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 16


# -----------------------
# COMMON FUNCTIONS
# -----------------------
def pad(data):
    padding = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding]) * padding


def generate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        sha256.update(f.read())
    return sha256.hexdigest()


# -----------------------
# AES ENCRYPT
# -----------------------
def aes_encrypt(file_path):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)

    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted = cipher.encrypt(pad(data))

    out_path = file_path + ".aes"

    with open(out_path, 'wb') as f:
        f.write(encrypted)

    return out_path


# -----------------------
# DES ENCRYPT
# -----------------------
def des_encrypt(file_path):
    key = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_ECB)

    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted = cipher.encrypt(pad(data))

    out_path = file_path + ".des"

    with open(out_path, 'wb') as f:
        f.write(encrypted)

    return out_path


# -----------------------
# BLOWFISH ENCRYPT
# -----------------------
def blowfish_encrypt(file_path):
    key = get_random_bytes(16)
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)

    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted = cipher.encrypt(pad(data))

    out_path = file_path + ".bf"

    with open(out_path, 'wb') as f:
        f.write(encrypted)

    return out_path


# -----------------------
# RSA ENCRYPT
# -----------------------
def rsa_encrypt(file_path):
    key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key.publickey())

    with open(file_path, 'rb') as f:
        data = f.read()

    # RSA works only on small data → trim
    encrypted = cipher.encrypt(data[:190])

    out_path = file_path + ".rsa"

    with open(out_path, 'wb') as f:
        f.write(encrypted)

    return out_path