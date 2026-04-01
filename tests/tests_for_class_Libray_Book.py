import pytest

from datetime import datetime
from classes import LibraryBook

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
