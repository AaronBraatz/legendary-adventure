"""Test for example functions."""
import pytest

from example.math_functions import add_int


def test_add_int():
    assert add_int(5, 5) == 10
    assert add_int(0, 10) == 10
    assert add_int(2, 8) == 10
    assert add_int(4, 6) == 10
    assert add_int(7, 3) == 10


def test_invalid_addition():
    with pytest.raises(TypeError):
        add_int(1, "zwei")
