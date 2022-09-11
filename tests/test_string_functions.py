"""Test for example functions."""
import pytest

from example.string_functions import give_greetings


@pytest.mark.parametrize("test_input,expected", [
    ('John', "Hello John!"),
    ('Maria', "Hello Maria!"),
])
def test_give_greetings_to_multiple_names(test_input, expected):
    assert give_greetings(test_input) == expected


def test_give_new_greeting_to_name():
    assert give_greetings('John', "Good morning {name}!") == "Good morning John!"
