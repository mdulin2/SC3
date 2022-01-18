import argparse
import random

UPPER_A_ORD = ord("A")
LOWER_A_ORD = ord("a")


def shift_upper(char: str, shift: int) -> str:
    """Shift an uppercase character."""
    char_ord = ord(char)
    char_ord = char_ord + shift - UPPER_A_ORD
    char_ord = char_ord % 26 + UPPER_A_ORD
    shifted_char = chr(char_ord)
    return shifted_char


def shift_lower(char: str, shift: int) -> str:
    """Shift a lowercase character."""
    char_ord = ord(char)
    char_ord = char_ord + shift - LOWER_A_ORD
    char_ord = char_ord % 26 + LOWER_A_ORD
    shifted_char = chr(char_ord)
    return shifted_char


def shift_char(char: str, shift: str) -> str:
    """Shift a character."""
    if char.isupper():
        char = shift_upper(char, shift)
    elif char.islower():
        char = shift_lower(char, shift)
    return char


def caesar_cipher(phrase: str, shift: int) -> str:
    """Caesar cipher encryption."""
    encrypted_phrase = "".join([
        shift_char(char, shift)
        for char
        in phrase
    ])
    return encrypted_phrase


def one_time_pad(phrase: str, seed: int) -> str:
    """One-time-pad encryption using a RNG seed."""
    random.seed(seed)
    encrypted_phrase = ""
    for char in phrase:
        shift = random.randint(0, 25)
        char = shift_char(char, shift)
        encrypted_phrase += char
    return encrypted_phrase


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Encrypt and decrypt some strings!")
    subparsers = parser.add_subparsers(dest="cmd")

    caeser_parser: argparse.ArgumentParser = subparsers.add_parser("caesar")
    caeser_parser.add_argument("phrase", help="{hrase to encrypt.")
    caeser_parser.add_argument("shift", type=int, help="Number of values to shift.")

    otp_parser: argparse.ArgumentParser = subparsers.add_parser("otp")
    otp_parser.add_argument("phrase", help="Phrase to encrypt.")
    otp_parser.add_argument("--seed", "-S", type=int, help="Seed for the random number generator.", default=42)

    cli_args = parser.parse_args()
    match cli_args.cmd:
        case "caesar":
            encrypted_phrase = caesar_cipher(cli_args.phrase, cli_args.shift)
            print(f"{cli_args.phrase} -> {encrypted_phrase}")
        case "otp":
            encrypted_phrase = one_time_pad(cli_args.phrase, cli_args.seed)
            print(f"{cli_args.phrase} -> {encrypted_phrase}")
