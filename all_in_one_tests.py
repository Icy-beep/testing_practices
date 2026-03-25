import pytest
from functions import unique, is_number, count_words, calculate_sum


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


def test_is_number():
    assert is_number('1') == True, 'Должен вернуть True - [1] является целым числом'


def test_is_number_str():
    assert is_number('w') == False, 'Должен вернуть False - [w] не является числом'


def test_is_number_with_space():
    assert is_number(' 1 ') == True, ('Должен вернуть True - [1] является числом пробелы справа и слева не должны'
                                      'учитываться если там только пробелы')


def test_is_number_with_space_middle():
    assert is_number('1 1') == False, ('Должен вернуть False - [1 1] это два целых числа наша функция проверяет'
                                       'является ли строка одним целым числом')


def test_is_number_float():
    assert is_number('1.2') == False, 'Должен вернуть False - [1.2] не является целым числом'


def test_is_number_void():
    assert is_number('') == False, 'Должен вернуть False - пустая строка не целое число'


def test_is_number_bool():
    assert is_number('True') == False, ('Должен вернуть False - хоть [True] и является целым числом [1] но это другой тип'
                                        'данных')


def test_is_number_list():
    assert is_number([1,2,3]) == False, 'функция не должна работать со списком'


def test_count_words_empty_string():
    assert count_words('') == 0, 'Должен вернуть 0 для пустой строки'


def test_count_words_whitespace_only():
    assert count_words('         ') == 0, 'Должен вернуть 0, если в строке только пробелы'


def test_count_words_multiple_spaces():
    assert count_words('a   b   c') == 3, 'Должен корректно считать слова с лишними пробелами между ними'

def test_count_words_with_punctuation():
    assert count_words('a, b, c.') == 3, 'Знаки препинания не должны считаться отдельными словами'


def test_count_words_with_numbers():
    assert count_words('1, 2, 3, no!') == 1, 'Числа не должны учитываться как слова, только буквенные последовательности'


def test_count_words_hyphenated_terms():
    assert count_words('a - b - c') == 3, 'Одиночные дефисы не должны считаться словами'


def test_count_words_single_letters():
    assert count_words('a') == 1, 'Одиночная буква является словом'


def test_count_words_single_symbol():
    assert count_words('*') == 0, 'Одиночный спецсимвол не является словом'


def test_count_words_invalid_type_raises_error():
    with pytest.raises(TypeError) as error_info:
        count_words(1)

    print(f"\nТекст ошибки: {error_info.value}")

    assert 'Функция работает только со строками' in str(error_info.value)


def test_sum_positive_integer():
    assert calculate_sum(3) == 6, 'Для n=3 сумма (1+2+3) должна быть 6'


def test_sum_float_input():
    assert calculate_sum(3.4) == 7.48, 'Должен корректно обрабатывать float'


def test_sum_numeric_string():
    assert calculate_sum('2') == 3, 'Должен уметь преобразовывать число-строку в число'


def test_sum_boundary_minimum():
    assert calculate_sum(1) == 1, 'Минимальное значение n=1 должно возвращать 1'


def test_sum_large_number():
    assert calculate_sum(10**10) == 5.0000000005e+19, 'Должен справляться с большими числами'


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