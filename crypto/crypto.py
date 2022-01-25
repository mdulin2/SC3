import argparse

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


def shift_char(char: str, shift: int) -> str:
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


def one_time_pad_encrypt(phrase: str, key: str) -> str:
    """One-time-pad encryption using a key."""
    if len(key) < len(phrase):
        raise ValueError("Key must be at least as long as phrase for encoding a OTP.")
    encrypted_phrase = ""
    for phrase_char, key_char in zip(phrase, key):
        is_upper = phrase_char.isupper()
        phrase_ord = ord(phrase_char.lower()) - LOWER_A_ORD
        key_ord = ord(key_char.lower()) - LOWER_A_ORD
        encrypted_ord = (phrase_ord + key_ord) % 26
        encrypted_char = chr(encrypted_ord + LOWER_A_ORD)
        encrypted_char = encrypted_char.upper() if is_upper else encrypted_char
        encrypted_phrase += encrypted_char
    return encrypted_phrase


def one_time_pad_decrypt(encrypted_phrase: str, key: str) -> str:
    """One-time-pad decryption using a key."""
    if len(key) < len(encrypted_phrase):
        raise ValueError("Key must be at least as long as encrypted phrase for decoding a OTP.")
    phrase = ""
    for encrypted_phrase_char, key_char in zip(encrypted_phrase, key):
        is_upper = encrypted_phrase_char.isupper()
        encrypted_phrase_ord = ord(encrypted_phrase_char.lower()) - LOWER_A_ORD
        key_ord = ord(key_char.lower()) - LOWER_A_ORD
        phrase_ord = (encrypted_phrase_ord - key_ord) % 26
        phrase_char = chr(phrase_ord + LOWER_A_ORD)
        phrase_char = phrase_char.upper() if is_upper else phrase_char
        phrase += phrase_char
    return phrase



if __name__ == "__main__":
    parser = argparse.ArgumentParser("Encrypt and decrypt some strings!")
    subparsers = parser.add_subparsers(dest="cmd")

    caeser_parser: argparse.ArgumentParser = subparsers.add_parser("caesar")
    caeser_parser.add_argument("phrase", help="{hrase to encrypt.")
    caeser_parser.add_argument("shift", type=int, help="Number of values to shift.")

    otp_parser: argparse.ArgumentParser = subparsers.add_parser("otp")
    otp_parser.add_argument("phrase", help="Phrase to encrypt.")
    otp_parser.add_argument("key", "-K", help="Key for the one-time-pad generator.", required=True)

    cli_args = parser.parse_args()
    match cli_args.cmd:
        case "caesar":
            encrypted_phrase = caesar_cipher(cli_args.phrase, cli_args.shift)
            print(f"{cli_args.phrase} -> {encrypted_phrase}")
        case "otp":
            encrypted_phrase = one_time_pad_encrypt(cli_args.phrase, cli_args.key)
            print(f"{cli_args.phrase} -> {encrypted_phrase}")
