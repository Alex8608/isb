import json
import logging

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

logging.basicConfig(level=logging.INFO)


class FileWork:
    """
    Class for work with files
    """
    def __init__(self, path: str) -> None:
        """
        Initialization
        :param path: str - path to file:
        :return None:
        """
        self.path = path

    def key_nonce_serializer(self, key: bytes) -> None:
        """
        Serialize the key or nonce and save it to file
        :param key: bytes - key or nonce to be serialized:
        :return None:
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(key)
        except Exception as e:
            logging.error(f"Error in key_nonce_serializer (FileWork) - {e}")

    def key_nonce_deserializer(self) -> bytes:
        """
        Deserialize the key or nonce from a file
        :return: bytes - deserialized key or nonce:
        """
        try:
            with open(self.path, 'rb') as file:
                return file.read()
        except Exception as e:
            logging.error(f"Error in key_nonce_deserializer (FileWork) - {e}")

    def serialize_private_key(self, private_key: rsa.RSAPrivateKey) -> None:
        """
        Serialize private key
        :param private_key: rsa.RSAPrivateKey - private key:
        :return None:
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                     encryption_algorithm=serialization.NoEncryption()))
        except Exception as e:
            logging.error(f"Error in serialize_private_key (FileWork) - {e}")

    def serialize_public_key(self, public_key: rsa.RSAPublicKey) -> None:
        """
        Serialize public key
        :param public_key: rsa.RSAPublicKey - public key:
        :return None:
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                   format=serialization.PublicFormat.SubjectPublicKeyInfo))
        except Exception as e:
            logging.error(f"Error in serialize_public_key (FileWork) - {e}")

    def deserialize_private_key(self) -> rsa.RSAPrivateKey:
        """
        Deserialize private key and return it
        :return rsa.RSAPrivateKey - deserialized private key:
        """
        try:
            with open(self.path, 'rb') as file:
                return serialization.load_pem_private_key(file.read(), password=None)
        except Exception as e:
            logging.error(f"Error in deserialize_private_key (FileWork) - {e}")

    def deserialize_public_key(self) -> rsa.RSAPublicKey:
        """
        Deserialize public key and return it
        :return rsa.RSAPublicKey - deserialized public key:
        """
        try:
            with open(self.path, 'rb') as file:
                return serialization.load_pem_public_key(file.read())
        except Exception as e:
            logging.error(f"Error in deserialize_public_key (FileWork) - {e}")

    def txt_reader(self, mode: str, encoding=None) -> str:
        """
        Reading txt file and return string from there
        :param mode: str - mode to open the file:
        :param encoding: - encoding of the text file, default = None:
        :return str from file:
        """
        try:
            with open(self.path, mode=mode, encoding=encoding) as file:
                return file.read()
        except Exception as e:
            logging.error(f"Error in txt_reader (FileWork) - {e}")

    def txt_writer(self, string: bytes) -> None:
        """
        Write string to file
        :param string: bytes - string that should be written
        :return None:
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(string)
        except Exception as e:
            logging.error(f"Error in txt_writer (FileWork) - {e}")

    def json_reader(self) -> dict:
        """
        Reading json file and return dict
        :return dict of data from json file:
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                paths = json.load(file)
            return paths
        except Exception as e:
            logging.error(f"Error in json_reader (FileWork) - {e}")
