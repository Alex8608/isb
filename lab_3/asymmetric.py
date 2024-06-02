import logging

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

logging.basicConfig(level=logging.INFO)


class Asymmetric:
    """
    Class for asymmetric cryptography operations
    (generating key pairs, encrypting and decrypting data)
    """

    def __init__(self, private_key_path: str, public_key_path: str) -> None:
        """
        Initialize AsymmetricCryptography object with public and private key path
        :param private_key_path: str - path to the private key file:
        :param public_key_path: str - path to the public key file:
        :return None:
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path

    @staticmethod
    def generate_key_pair(key_len: int) -> tuple:
        """
        Generate RSA key pair
        :param key_len: int - len of the RSA key in bits:
        :return tuple containing private and public keys:
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_len)
        public_key = private_key.public_key()
        return private_key, public_key

    def serialize_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serialize private key
        :param private_key: rsa.RSAPrivateKey - private key:
        :return None:
        """
        try:
            with open(self.private_key_path, 'wb') as file:
                file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                     encryption_algorithm=serialization.NoEncryption()))
        except Exception as e:
            logging.error(f"Error in serialize_private_key (Asymmetric) - {e}")

    def serialize_public_key(self, public_key: rsa.RSAPublicKey) -> None:
        """
        Serialize public key
        :param public_key: rsa.RSAPublicKey - public key:
        :return None:
        """
        try:
            with open(self.public_key_path, 'wb') as file:
                file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                   format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except Exception as e:
            logging.error(f"Error in serialize_public_key (Asymmetric) - {e}")

    def deserialize_private_key(self) -> rsa.RSAPrivateKey:
        """
        Deserialize private key and return it
        :return rsa.RSAPrivateKey - deserialized private key:
        """
        try:
            with open(self.private_key_path, 'rb') as file:
                return serialization.load_pem_private_key(file.read(), password=None)
        except Exception as e:
            logging.error(f"Error in deserialize_private_key (Asymmetric) - {e}")

    def deserialize_public_key(self) -> rsa.RSAPublicKey:
        """
        Deserialize public key and return it
        :return rsa.RSAPublicKey - deserialized public key:
        """
        try:
            with open(self.public_key_path, 'rb') as file:
                return serialization.load_pem_public_key(file.read())
        except Exception as e:
            logging.error(f"Error in deserialize_public_key (Asymmetric) - {e}")

    @staticmethod
    def decrypt_with_private_key(private_key: rsa.RSAPrivateKey, text: bytes) -> bytes:
        """
        Decrypting text using provided private key
        :param private_key: rsa.RSAPrivateKey - RSA private key used for decryption:
        :param text: str - text to be decrypted:
        :return bytes - text produced by decryption process:
        """
        return private_key.decrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                      algorithm=hashes.SHA256(), label=None))

    @staticmethod
    def encrypt_with_public_key(public_key: rsa.RSAPublicKey, text: bytes) -> bytes:
        """
        Encrypting text using the provided public key
        :param public_key: rsa.RSAPublicKey - RSA public key used for encryption:
        :param text: str - text to be encrypted:
        :return bytes - text produced by encryption process:
        """
        return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                     algorithm=hashes.SHA256(), label=None))
