# encryptie_app.py

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

backend = default_backend()


def derive_key(password: str, salt: bytes) -> bytes:
    """Genereert een AES-sleutel uit een wachtwoord en salt met PBKDF2"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256
        salt=salt,
        iterations=100_000,
        backend=backend
    )
    return kdf.derive(password.encode())