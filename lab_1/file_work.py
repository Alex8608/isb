import logging
import json

logging.basicConfig(level=logging.INFO)


def json_reader(path: str) -> dict:
    """
    Reading json file and return dict
    :param path: str - path to json file:
    :return dict of data from json file:
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            paths = json.load(file)
        return paths
    except Exception as e:
        logging.error(f"Error in json_reader - {e}")


def json_writer(path: str, res: dict) -> None:
    """
    Write dict into json file
    :param path: str - path to json file:
    :param res: dict - dictionary that should be written:
    :return None:

    """
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(res, file, indent=4, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Error in json_writer - {e}")


def txt_writer(path: str, string: str) -> None:
    """
    Write string to file
    :param path: str - path to writing file
    :param string: str - string that should be written
    :return None:
    """
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(string)
    except Exception as e:
        logging.error(f"Error in txt_writer - {e}")


def txt_reader(path: str) -> str:
    """
    Reading txt file and return string from there
    :param path: str - path to txt file:
    :return str from file:
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            string = file.read()
        return string
    except Exception as e:
        logging.error(f"Error in txt_reader - {e}")