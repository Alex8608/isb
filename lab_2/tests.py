import logging
import math
import mpmath

from constants import MAX_LENGTH_BLOCK, PI, SEQUENCES_PATH
from file_work import json_reader

logging.basicConfig(level=logging.INFO)


def frequency_bitwise_test(sequence: str) -> float:
    """
    Finding the frequency bitwise test and return the p-value
    :param sequence: str - input binary sequence:
    :return float - p-value of the test:
    """
    try:
        sum_bits = sum(1 if bit == '1' else -1 for bit in sequence)
        s_n = math.fabs(sum_bits) / math.sqrt(len(sequence))
        p_value = math.erfc(s_n / math.sqrt(2))
        return p_value
    except Exception as e:
        logging.error(f"Error in frequency_bitwise_test: {e}\n")


def same_consecutive_bits_test(sequence: str) -> float:
    """
    Finding the same consecutive bits test and return the p-value
    :param sequence: str - input binary sequence:
    :return float - p-value of the test:
    """
    try:
        fate_of_ones = sequence.count('1') / len(sequence)
        if abs(fate_of_ones - 0.5) >= (2 / math.sqrt(len(sequence))):
            return 0
        v_n = 0
        v_n += sum(1 if sequence[i] != sequence[i + 1] else 0 for i in range(len(sequence) - 1))
        p_value = math.erfc(abs(v_n - 2 * len(sequence) * fate_of_ones * (1 - fate_of_ones)) / (
                2 * math.sqrt(2 * len(sequence)) * fate_of_ones * (1 - fate_of_ones)))
        return p_value
    except Exception as e:
        logging.error(f"Error in same_consecutive_bits_test: {e}\n")


def longest_sequence_in_block_test(sequence: str) -> float:
    """
    Finding the longest sequence of ones in a block test and return the p-value
    :param sequence: str - input binary sequence:
    :return float - p-value of the test:
    """
    try:
        max_len_in_block = {}
        for step in range(0, len(sequence), MAX_LENGTH_BLOCK):
            block = sequence[step:step + MAX_LENGTH_BLOCK]
            max_length, length = 0, 0
            for bit in block:
                length = length + 1 if bit == "1" else 0
                max_length = max(max_length, length)
            max_len_in_block[max_length] = max_len_in_block.get(max_length, 0) + 1
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for i in max_len_in_block:
            key = min(i, 4)
            v[key] += max_len_in_block[i]
        hi_square = 0
        for i in range(4):
            hi_square += math.pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        return mpmath.gammainc(3 / 2, hi_square / 2)
    except Exception as e:
        logging.error(f"Error in longest_sequence_in_block_test: {e}\n")


if __name__ == "__main__":
    sequences = json_reader(SEQUENCES_PATH)

    logging.info("frequency bitwise test result for C++: %s", frequency_bitwise_test(sequences["cpp"]))
    logging.info("same consecutive bits test result for C++: %s", same_consecutive_bits_test(sequences["cpp"]))
    logging.info("longest sequence in block test result for C++: %s", longest_sequence_in_block_test(sequences["cpp"]))

    logging.info("frequency bitwise test result for Java: %s", frequency_bitwise_test(sequences["java"]))
    logging.info("same consecutive bits test result for Java: %s", same_consecutive_bits_test(sequences["java"]))
    logging.info("longest sequence in block test result for Java: %s",
                 longest_sequence_in_block_test(sequences["java"]))