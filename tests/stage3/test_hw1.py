import pytest

from src.stage3.hw1 import is_lucky


@pytest.mark.parametrize(
    "ticket,expected",
    [
        ("090234", True),
        ("123456", False),
    ],
)
def test_is_lucky(ticket, expected):
    assert is_lucky(ticket) == expected
