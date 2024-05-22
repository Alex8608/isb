import json
import logging

logging.basicConfig(level=logging.INFO)


class FileWork:
    def __init__(self, path: str) -> None:
        """
        Initialization
        :param path: str - path to file:
        :return None:
        """
        self.path = path

    def key_serializer(self, key: bytes) -> None:
        """
        Serialize the key and save it to file
        :param key: bytes - key to be serialized:
        :return None:
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(key)
        except Exception as e:
            logging.error(f"Error in key_serializer - {e}")

    def key_deserializer(self) -> bytes:
        """
        Deserialize the key from a file
        :return: bytes - deserialized key:
        """
        try:
            with open(self.path, 'rb') as file:
                return file.read()
        except Exception as e:
            logging.error(f"Error in key_deserializer - {e}")

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
            logging.error(f"Error in txt_reader - {e}")

    def txt_writer(self, string: str) -> None:
        """
        Write string to file
        :param string: str - string that should be written
        :return None:
        """
        try:
            with open(self.path, 'wb') as file:
                file.write(string)
        except Exception as e:
            logging.error(f"Error in txt_writer - {e}")

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
            logging.error(f"Error in json_reader - {e}")
