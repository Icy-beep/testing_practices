import pytest
from classes import Temperature

@pytest.fixture
def temp_zero():
    """Фикстура для нулевой температуры"""
    return Temperature(0)

@pytest.fixture
def temp_hot():
    """Фикстура для высокой температуры"""
    return Temperature(100)

@pytest.fixture
def temp_below_zero():
    """Фикстура для отрицательной температуры"""
    return Temperature(-20)

# 1. Проверка корректности инициализации и получения значения для нулевой температуры
def test_init_and_get_value_zero(temp_zero):
    assert temp_zero.get_value() == 0

# 2. Проверка корректности инициализации и получения значения для высокой температуры
def test_init_and_get_value_hot(temp_hot):
    assert temp_hot.get_value() == 100

# 3. Тест перевода 0°C в градусы Фаренгейта
def test_to_fahrenheit_zero(temp_zero):
    assert temp_zero.to_fahrenheit() == 32

# 4. Тест перевода 100°C в градусы Фаренгейта
def test_to_fahrenheit_hot(temp_hot):
    assert temp_hot.to_fahrenheit() == 212

# 5. Тест перевода 0°C в Кельвины
def test_to_kelvin_zero(temp_zero):
    assert temp_zero.to_kelvin() == 273

# 6. Тест перевода 100°C в Кельвины
def test_to_kelvin_hot(temp_hot):
    assert temp_hot.to_kelvin() == 373

# 7. Проверка, что положительная температура определяется верно
def test_is_positive_true(temp_hot):
    assert temp_hot.is_positive() == True

# 8. Проверка, что отрицательная температура не считается положительной
def test_is_positive_false(temp_below_zero):
    assert temp_below_zero.is_positive() == False

# 9. Сравнение двух температур, где первая больше второй
def test_compare_t1_bigger(temp_hot, temp_below_zero):
    t1 = temp_hot
    t2 = temp_below_zero
    assert Temperature.compare(t1, t2) == -1

# 10. Сравнение двух одинаковых температур
def test_compare_equal(temp_hot):
    t1 = temp_hot
    t2 = temp_hot
    assert Temperature.compare(t1, t2) == 0

# 11. Сравнение двух температур, где первая меньше второй
def test_compare_t1_smaller(temp_below_zero, temp_hot):
    t1 = temp_below_zero
    t2 = temp_hot
    assert Temperature.compare(t1, t2) == 1

# 12. Проверка генерации ошибки при попытке создать температуру ниже абсолютного нуля
def test_below_absolute_zero():
    with pytest.raises(ValueError):
        Temperature(-2000)

# 13. Проверка генерации ошибки при попытке создать температуру выше планковской температуры
def test_above_plank_temp():
    with pytest.raises(ValueError):
        Temperature(1.4168e320)