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
    "phrase, shift, expected",
    (
        ("zork", 0, "lmel"),
        ("zork", 42, "trrh"),
    )
)
def test__one_time_pad(phrase: str, shift: int, expected: str):
    assert expected == crypto.one_time_pad(phrase, shift)
