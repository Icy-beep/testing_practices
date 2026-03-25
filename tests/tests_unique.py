import pytest
from functions import unique

def test_unique_empty():
    assert unique([]) == [], "Должен возвращать пустой список"


def test_unique_no_duplicates():
    assert unique([1, "a", 2.5]) == [1, "a", 2.5], "Не должен изменять список без дублей"


def test_unique_integers():
    assert unique([1, 2, 2, 3, 3, 3]) == [1, 2, 3], "Должен оставлять только уникальные int"


def test_unique_strings():
    assert unique(["apple", "apple", "banana"]) == ["apple", "banana"], "Должен удалять дубликаты строк"


def test_unique_floats():
    assert unique([1.1, 1.1, 2.2]) == [1.1, 2.2], "Должен корректно работать с float"


def test_unique_mixed_types():
    # Учитываем, что в Python 1 == 1.0
    assert unique([1, 1.0, "1"]) == [1, "1"], "Должен учитывать равенство 1 и 1.0"


def test_unique_order():
    assert unique(["b", "a", "b", "c", "a"]) == ["b", "a", "c"], "Порядок должен соответствовать первому появлению"


def test_unique_long_list():
    long_list = [1, 2, 3] * 100
    assert unique(long_list) == [1, 2, 3], "Должен эффективно обрабатывать длинные списки"


def test_unique_type_error():
    with pytest.raises(TypeError):
        unique("not a list")