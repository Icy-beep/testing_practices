import pytest

from functions import is_number


def test_is_number():
    assert is_number('1') == True

def test_is_number_str():
    assert is_number('w') == False

def test_is_number_with_space():
    assert is_number(' 1 ') == True

def test_is_number_with_space_middle():
    assert is_number('1 1') == False

def test_is_number_float():
    assert is_number('1.2') == False

def test_is_number_void():
    assert is_number('') == False

def test_is_number_bool():
    assert is_number('true') == False

def test_is_number_list():
    assert is_number([1,2,3]) == True