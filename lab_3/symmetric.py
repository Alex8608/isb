import logging
import os
import struct

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from file_key_work import FileWork

logging.basicConfig(level=logging.INFO)


class Symmetric:
    """
    Class for symmetric cryptography operations
    (generating symmetric keys, encrypting and decrypting data)
    """

    def __init__(self, len_of_key: int, nonce_path: str) -> None:
        """
        Initialize SymmetricCryptography object with key length and nonce path
        :param len_of_key: int - length of the key:
        :param nonce_path: str - path to nonce:
        :return None:
        """
        self.key_len = len_of_key
        self.nonce_path = nonce_path

    def generate_key(self) -> bytes:
        """
        Generate and return symmetric key
        :return bytes - symmetric key:
        """
        return os.urandom(self.key_len // 8)

    def encrypt_text(self, symmetric_key: bytes, text: bytes) -> bytes:
        """
        Serialize nonce and encrypting the text using the provided symmetric key
        :param symmetric_key: bytes - symmetric key:
        :param text: bytes - text that should be encrypted:
        :return bytes - encrypted text:
        """
        try:
            nonce = os.urandom(8)
            counter = 0
            full_nonce = struct.pack("<Q", counter) + nonce
            FileWork(self.nonce_path).key_nonce_serializer(full_nonce)
            cipher = Cipher(algorithms.ChaCha20(symmetric_key, full_nonce), mode=None)
            encryptor = cipher.encryptor()
            return encryptor.update(text)

        except Exception as e:
            logging.error(f"Error in encrypt_text (Symmetric) - {e}")

    def decrypt_text(self, symmetric_key: bytes, text: bytes) -> bytes:
        """
        Decrypting the text using the provided symmetric key and deserialized nonce
        :param symmetric_key: bytes - symmetric key:
        :param text: bytes -  text that should be decrypted:
        :return bytes - decrypted text:
        """
        try:
            nonce = FileWork(self.nonce_path).key_nonce_deserializer()
            cipher = Cipher(algorithms.ChaCha20(symmetric_key, nonce), mode=None)
            decrypter = cipher.decryptor()
            return decrypter.update(text)

        except Exception as e:
            logging.error(f"Error in decrypt_text (Symmetric) - {e}")
