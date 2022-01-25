import pytest

from . import crypto


@pytest.mark.parametrize(
    "phrase, shift, expected",
    (
        ("zork", 0, "zork"),
        ("zork", 1, "apsl"),
        ("zork", -1, "ynqj"),
    )
)
def test__caesar_cipher(phrase: str, shift: int, expected: str):
    assert expected == crypto.caesar_cipher(phrase, shift)


@pytest.mark.parametrize(
    "phrase, key, expected",
    (
        ("hello", "xmckl", "eqnvz"),
        ("HELLO", "XMCKL", "EQNVZ"),
    )
)
def test__one_time_pad_encrypt(phrase: str, key: str, expected: str):
    assert expected == crypto.one_time_pad_encrypt(phrase, key)


@pytest.mark.parametrize(
    "encrypted_phrase, key, expected",
    (
        ("eqnvz", "xmckl", "hello"),
        ("EQNVZ", "XMCKL", "HELLO"),
    )
)
def test__one_time_pad_decrypt(encrypted_phrase: str, key: str, expected: str):
    assert expected == crypto.one_time_pad_decrypt(encrypted_phrase, key)


@pytest.mark.parametrize(
    "phrase, key",
    (
        ("eqnvz", "xmckl"),
        ("EQNVZ", "XMCKL"),
    )
)
def test__one_time_pad(phrase: str, key: str):
    assert phrase == crypto.one_time_pad_decrypt(crypto.one_time_pad_encrypt(phrase, key), key)

