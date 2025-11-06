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

def encrypt(plaintext: str, password: str) -> str:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=backend)
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    encrypted_data = salt + iv + ciphertext
    return base64.b64encode(encrypted_data).decode()

def main():
    print("Symmetrische Encryptie CLI-app (AES-256)")
    choice = input("Typ 'e' om te versleutelen of 'd' om te ontsleutelen: ").lower()

    if choice == 'e':
        text = input("Voer de tekst in die je wilt versleutelen: ")
        password = input("Voer een wachtwoord in: ")
        encrypted = encrypt(text, password)
        print("\nVersleutelde tekst:")
        print(encrypted)

    elif choice == 'd':
        encrypted_text = input("Voer de versleutelde tekst in: ")
        password = input("Voer het wachtwoord in: ")
        try:
            decrypted = decrypt(encrypted_text, password)
            print("\nOntsleutelde tekst:")
            print(decrypted)
        except Exception:
            print("Fout bij ontsleutelen. Controleer je wachtwoord en de tekst.")

    else:
        print("Ongeldige keuze. Sluiten...")

if __name__ == "__main__":
    main()
