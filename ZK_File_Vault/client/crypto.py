# client/crypto.py
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from argon2.low_level import hash_secret_raw, Type
import os

def derive_key(password):
    salt = b'static_salt'  # for demo; improve later
    return hash_secret_raw(
        password.encode(),
        salt,
        time_cost=2,
        memory_cost=102400,
        parallelism=8,
        hash_len=32,
        type=Type.ID
    )

def encrypt(data, key):
    aes = AESGCM(key)
    nonce = os.urandom(12)
    ct = aes.encrypt(nonce, data, None)
    return nonce + ct

def decrypt(data, key):
    nonce = data[:12]
    ct = data[12:]
    aes = AESGCM(key)
    return aes.decrypt(nonce, ct, None)