import pytest

from functions import count_words

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