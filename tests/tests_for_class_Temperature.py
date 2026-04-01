import pytest
from classes import Temperature

@pytest.fixture
def temp_zero():
    return Temperature(0)

@pytest.fixture
def temp_hot():
    return Temperature(100)

@pytest.fixture
def temp_below_zero():
    return Temperature(-20)

def test_init_and_get_value_zero(temp_zero):
    assert temp_zero.get_value() == 0

def test_init_and_get_value_hot(temp_hot):
    assert temp_hot.get_value() == 100

def test_to_fahrenheit_zero(temp_zero):
    assert temp_zero.to_fahrenheit() == 32

def test_to_fahrenheit_hot(temp_hot):
    assert temp_hot.to_fahrenheit() == 212

def test_to_kelvin_zero(temp_zero):
    assert temp_zero.to_kelvin() == 273

def test_to_kelvin_hot(temp_hot):
    assert temp_hot.to_kelvin() == 373

def test_is_positive_true(temp_hot):
    assert temp_hot.is_positive() == True

def test_is_positive_false(temp_below_zero):
    assert temp_below_zero.is_positive() == False

def test_compare_t1_bigger(temp_hot, temp_below_zero):
    t1 = temp_hot
    t2 = temp_below_zero
    assert Temperature.compare(t1, t2) == -1

def test_compare_equal(temp_hot):
    t1 = temp_hot
    t2 = temp_hot
    assert Temperature.compare(t1, t2) == 0

def test_compare_t1_smaller(temp_below_zero, temp_hot):
    t1 = temp_below_zero
    t2 = temp_hot
    assert Temperature.compare(t1, t2) == 1

def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-2000)

def test_above_plank_temp():
    with pytest.raises(ValueError):
        Temperature(1.4168e320)
