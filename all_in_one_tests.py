import pytest

from datetime import datetime
from classes import LibraryBook, Temperature

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



@pytest.fixture
def classic_book():
    """Фикстура для старой книги (например, 1949 год)"""
    return LibraryBook("1984", "George Orwell", 1949)

@pytest.fixture
def modern_book():
    """Фикстура для новой книги (вышла в текущем году)"""
    current_year = datetime.now().year
    return LibraryBook("Python Guide", "Dmitry Rak", current_year)

@pytest.fixture
def current_year():
    """Фикстура для текущего года"""
    current_year = datetime.now().year
    return current_year

# 1. Проверка инициализации названия
def test_title_init(classic_book):
    assert classic_book.get_title() == "1984"

# 2. Проверка инициализации автора
def test_author_init(classic_book):
    assert classic_book.get_author() == "George Orwell"

# 3. Проверка инициализации года
def test_year_init(classic_book):
    assert classic_book.get_publish_year() == 1949

# 4. Проверка метода rename
def test_rename_functionality(modern_book):
    modern_book.rename("Python is cool")
    assert modern_book.get_title() == "Python is cool"

# 5. Проверка __str__: наличие названия
def test_str_contains_title(classic_book):
    assert "1984" in str(classic_book)

# 6. Проверка __str__: наличие автора
def test_str_contains_author(classic_book):
    assert "George Orwell" in str(classic_book)

# 7. Проверка __str__: корректный формат строк
def test_str_format(modern_book):
    output = str(modern_book)
    assert "Название книги:" in output
    assert "Автор:" in output
    assert "Год выхода:" in output

# 8. Проверка метода age для старой книги
def test_age_calculation_old(classic_book):
    expected_age = datetime.now().year - 1949
    assert classic_book.age() == expected_age

# 9. Проверка метода age для новой книги
def test_age_calculation_new(modern_book):
    assert modern_book.age() == 0

# 10. Проверка is_old для классики (должно быть True, так как > 50 лет)
def test_is_old_true(classic_book):
    assert classic_book.is_old() is True

# 11. Проверка is_old для новой книги (должно быть False)
def test_is_old_false(modern_book):
    assert modern_book.is_old() is False

# 12. Проверка, что геттер возвращает именно число (int)
def test_year_type(modern_book):
    assert isinstance(modern_book.get_publish_year(), int)

# 13. Работа rename после нескольких смен
def test_multiple_renames(classic_book):
    classic_book.rename("84")
    classic_book.rename("Nineteen Eighty-Four")
    assert classic_book.get_title() == "Nineteen Eighty-Four"

# 14. Ошибка при пустом названии
def test_init_empty_title():
    with pytest.raises(ValueError, match="Название книги"):
        LibraryBook("", "Author", 2000)

# 15. Ошибка при пустом авторе
def test_init_whitespace_author():
    with pytest.raises(ValueError, match="Имя автора"):
        LibraryBook("Title", "   ", 2000)

# 16. Ошибка при годе издания в будущем
def test_init_future_year(current_year):
    with pytest.raises(ValueError, match="не может быть больше текущего"):
        LibraryBook("Future", "Author", current_year + 1)

# 17. Ошибка при попытке переименовать в пустую строку
def test_rename_error(classic_book):
    with pytest.raises(ValueError, match="не может быть пустым"):
        classic_book.rename("  ")

# 18. Ошибка в методе age, если передан год меньше года издания
def test_age_error(classic_book):
    with pytest.raises(ValueError, match="не может быть меньше года издания"):
        classic_book.age(1900)
