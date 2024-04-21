import logging
import argparse

from constants import ALPHABET, PATHS
from file_work import json_reader, txt_writer, txt_reader

logging.basicConfig(level=logging.INFO)


def encrypting(keyword: str, text: str) -> str:
    """
    Encrypt text using the Vision table and
    :param keyword: str - keyword for encrypting:
    :param text: str - string that should be encrypted:
    :return str - encrypted string:
    """
    encrypted_str = ""
    try:
        key_all_string = keyword * (len(text) // len(keyword)) + keyword[:len(text) % len(keyword)]
        for letter, key in zip(text, key_all_string):
            encrypted_str += ''.join((symbol for symbol, index in ALPHABET.items()
                                      if index == (ALPHABET[letter] + ALPHABET[key]) % 33))
        return encrypted_str
    except Exception as e:
        logging.error(f"Error in encrypting function - {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keyword', type=str, required=True)
    try:
        args = parser.parse_args()
    except argparse.ArgumentError:
        logging.error("ArgumentError")
    KEYWORD = args.keyword
    paths = json_reader(PATHS)
    txt_writer(paths["encrypted"], encrypting(KEYWORD, txt_reader(paths["input1"])))
    txt_writer(paths["key1"], f"KEYWORD: {KEYWORD}")
