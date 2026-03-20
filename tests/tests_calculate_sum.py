import pytest

from functions import calculate_sum

def test_sum_positive_integer():
    assert calculate_sum(3) == 6

def test_sum_float_input():
    assert calculate_sum(3.4) == 7.48

def test_sum_numeric_string():
    assert calculate_sum('2') == 3

def test_sum_boundary_minimum():
    assert calculate_sum(1) == 1

def test_sum_large_number():
    assert calculate_sum(10**10) == 5.0000000005e+19

def test_error_zero():
    with pytest.raises(ValueError):
        calculate_sum(0)

def test_error_less_than_one():
    with pytest.raises(ValueError) as error_info:
        calculate_sum(-2)

    print(f"\nТекст ошибки: {error_info.value}")

    assert "n не должен быть меньше 1" in str(error_info.value)

def test_error_invalid_string():
    with pytest.raises(ValueError) as error_info:
        calculate_sum("привет")

    print(f"\nТекст ошибки: {error_info.value}")

    assert "невозможно преобразовать n в число" in str(error_info.value)