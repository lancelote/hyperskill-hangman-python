import pytest

from src.stage3.hw2 import fits


@pytest.mark.parametrize(
    "params,expected",
    [
        ([24, 21, 11, 36, 80], True),
        ([80, 50, 80, 33, 78], False),
    ],
)
def test_fits(params, expected):
    assert fits(*params) == expected
