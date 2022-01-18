from .add_function import add_int


def test_simple_addition():
    assert add_int(2, 3) == 5


def test_negative_addition():
    assert add_int(-5, 10) == 5


def test_invalid_input():
    assert add_int(2, None) == 2


def test_string_input():
    assert add_int(2, "2") == 4
