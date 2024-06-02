import argparse
import logging

from hybrid import Hybrid
from symmetric import Symmetric
from asymmetric import Asymmetric
from file_key_work import FileWork
from constants import PATHS


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Entry point of the program")
    all_paths = FileWork(PATHS)
    paths_dict = all_paths.json_reader()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-key', '--keys',
                       action='store_true',
                       help='Run key generation mode')
    group.add_argument('-enc', '--encryption',
                       action='store_true',
                       help='Run encryption mode')
    group.add_argument('-dec', '--decryption',
                       action='store_true',
                       help='Run decryption mode')
    parser.add_argument('-text', '--input_text_file',
                        type=str,
                        default=paths_dict["initial_file"],
                        help='Path to the input txt file with text (default: paths_dict["initial_file"]')
    parser.add_argument('-public_key', '--public_key_path',
                        type=str,
                        default=paths_dict["public_key"],
                        help='Path to the public pem file with key (default: paths_dict["public_key"]')
    parser.add_argument('-private_key', '--private_key_path',
                        type=str,
                        default=paths_dict["private_key"],
                        help='Path to the private pem file with key (default: paths_dict["private_key"]')
    parser.add_argument('-sym_key', '--symmetric_key_path',
                        type=str,
                        default=paths_dict["symmetric_key_file"],
                        help='Path to the symmetric txt file with key (default: paths_dict["symmetric_key_file"]')
    parser.add_argument('-enc_path', '--encrypted_text_path',
                        type=str,
                        default=paths_dict["encrypted_file"],
                        help='Path to the txt file with encrypted text (default: paths_dict["encrypted_file"]')
    parser.add_argument('-dec_path', '--decrypted_text_path',
                        type=str,
                        default=paths_dict["decrypted_file"],
                        help='Path to the txt file with decrypted text (default: paths_dict["decrypted_file"]')
    parser.add_argument('-nonce_path', '--nonce_text_path',
                        type=str,
                        default=paths_dict["nonce_file"],
                        help='Path to the txt file with nonce for symmetric (default: paths_dict["nonce_file"]')
    try:
        args = parser.parse_args()
        symmetric_class = Symmetric(256, args.nonce_text_path)
        asymmetric_class = Asymmetric(args.private_key_path, args.public_key_path)
        hybrid = Hybrid(args.input_text_file, args.symmetric_key_path, args.encrypted_text_path,
                        args.decrypted_text_path, symmetric_class, asymmetric_class)
        match args:
            case args if args.keys:
                hybrid.generate_keys()

            case args if args.encryption:
                hybrid.encrypt_text()

            case args if args.decryption:
                hybrid.decrypt_text()

    except Exception as e:
        logging.error(f"Error in main: {e}")
