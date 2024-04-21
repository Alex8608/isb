import logging
import argparse

from constants import PATHS, FREQUENCY
from file_work import json_reader, json_writer, txt_writer, txt_reader

logging.basicConfig(level=logging.INFO)


def frequency(text: str) -> list:
    """
    Counting frequency of every symbol in string
    :param text: str - string where need count frequency of symbols:
    :return list - list of tuples (symbol, frequency):
    """
    try:
        return sorted({symbol: text.count(symbol) / len(text) for symbol in set(text)}.items(),
                      key=lambda item: item[1], reverse=True)
    except Exception as e:
        logging.error(f"Error in frequency function - {e}")


def make_key_dict(e_list: list, b_list: list) -> dict:
    """
    Make approximate key dictionary from 2 lists using frequency
    :param e_list: list - list with symbols from encrypted text:
    :param b_list: list - list with symbols from manual:
    :return dict {encrypted symbol: base symbol}:
    """
    k_dict = {}
    try:
        for i in range(len(e_list)):
            k_dict.update({e_list[i][0]: b_list[i][0]})
        return k_dict
    except Exception as e:
        logging.error(f"Error in make_key_dict function - {e}")


def decrypting(text: str, key_symbols: dict) -> str:
    """
    Decrypting text using frequency analysis algorithm
    :param text: str - encrypted string:
    :param key_symbols: dict - dictionary {encrypted symbol: base symbol}:
    :return str - decrypted string:
    """
    decrypted_list = []
    try:
        for symbol in text:
            decrypted_list.append(key_symbols[symbol])
        return ''.join(decrypted_list)
    except Exception as e:
        logging.error(f"Error in decrypting function - {e}")


if __name__ == "__main__":
    paths = json_reader(PATHS)
    encrypted_string = txt_reader(paths["input2"])
    encrypted_symbols_list = frequency(encrypted_string)
    base_symbols_list = sorted(FREQUENCY.items(), key=lambda item: item[1], reverse=True)
    # key_dict = make_key_dict(encrypted_symbols_list, base_symbols_list)
    # json_writer(paths["key2"], key_dict)
    txt_writer(paths["decrypted"], decrypting(encrypted_string, json_reader(paths["key2"])))
