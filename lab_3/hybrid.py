import logging

from symmetric import Symmetric
from asymmetric import Asymmetric
from file_key_work import FileWork

logging.basicConfig(level=logging.INFO)


class Hybrid:
    """
    Class for hybrid encryption using both symmetric and asymmetric keys
    """

    def __init__(self, text_path: str, symmetric_key_path: str, encrypted_text_path: str, decrypted_text_path: str,
                 symmetric_class: Symmetric, asymmetric_class: Asymmetric) -> None:
        """
        Initialize HybridCryptograpy object with necessary paths and key length
        :param text_path: str - path to initial file:
        :param symmetric_key_path: str - path to symmetric key file:
        :param encrypted_text_path: str - path to encrypted text file:
        :param decrypted_text_path: str - path to decrypted text file:
        :param symmetric_class: Symmetric - class instance for working with symmetric cryptography:
        :param asymmetric_class: Asymmetric - class instance for working with asymmetric cryptography:
        :return None:
        """
        self.text_path = text_path
        self.symmetric_key_path = symmetric_key_path
        self.encrypted_text_path = encrypted_text_path
        self.decrypted_text_path = decrypted_text_path
        self.symmetric_class = symmetric_class
        self.asymmetric_class = asymmetric_class

    def generate_keys(self) -> None:
        """
        Generating asymmetric and symmetric keys and serialize them
        :return None:
        """
        try:
            symmetric_key = self.symmetric_class.generate_key()
            private_key, public_key = self.asymmetric_class.generate_key_pair(2048)
            self.asymmetric_class.serialize_private_key(private_key)
            self.asymmetric_class.serialize_public_key(public_key)
            encrypted_symmetric_key = self.asymmetric_class.encrypt_with_public_key(public_key, symmetric_key)
            key = FileWork(self.symmetric_key_path)
            key.key_nonce_serializer(encrypted_symmetric_key)

            logging.info("Keys successfully generated and serialized")
        except Exception as e:
            logging.error(f"Error in generate_keys (Hybrid): {e}")

    def encrypt_text(self) -> None:
        """
        Encrypting the text using encrypted generated symmetric key and serialize it
        :return None:
        """
        try:
            key_file = FileWork(self.symmetric_key_path)
            encrypted_symmetric_key = key_file.key_nonce_deserializer()
            encrypted_symmetric_key = self.asymmetric_class.decrypt_with_private_key(
                self.asymmetric_class.deserialize_private_key(), encrypted_symmetric_key)
            text_file = FileWork(self.text_path)
            text = bytes(text_file.txt_reader("r", "UTF-8"), "UTF-8")
            encrypted_text = self.symmetric_class.encrypt_text(encrypted_symmetric_key, text)
            encrypted_text_file = FileWork(self.encrypted_text_path)
            encrypted_text_file.txt_writer(encrypted_text)
            logging.info("Text successfully encrypted and serialized")
        except Exception as e:
            logging.error(f"Error in encrypt_text (Hybrid): {e}")

    def decrypt_text(self) -> None:
        """
        Decrypting the text using encrypted generated symmetric key and serialize it
        :return None:
        """
        try:
            key_file = FileWork(self.symmetric_key_path)
            encrypted_symmetric_key = key_file.key_nonce_deserializer()
            encrypted_symmetric_key = self.asymmetric_class.decrypt_with_private_key(
                self.asymmetric_class.deserialize_private_key(), encrypted_symmetric_key)
            encrypted_text_file = FileWork(self.encrypted_text_path)
            encrypted_text = bytes(encrypted_text_file.txt_reader("rb"))
            decrypted_text = self.symmetric_class.decrypt_text(encrypted_symmetric_key, encrypted_text)
            decrypted_text_file = FileWork(self.decrypted_text_path)
            decrypted_text_file.txt_writer(decrypted_text)
            logging.info("Text successfully decrypted and serialized")
        except Exception as e:
            logging.error(f"Error in decrypt_text (Hybrid): {e}")
