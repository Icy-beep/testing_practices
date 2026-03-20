import pytest

from functions import count_words

def test_count_words_empty_string():
    assert count_words('') == 0

def test_count_words_whitespace_only():
    assert count_words('         ') == 0

def test_count_words_multiple_spaces():
    assert count_words('a   b   c') == 3

def test_count_words_with_punctuation():
    assert count_words('a, b, c.') == 3

def test_count_words_with_numbers():
    assert count_words('1, 2, 3, no!') == 1

def test_count_words_hyphenated_terms():
    assert count_words('a - b - c') == 3

def test_count_words_single_letters():
    assert count_words('a') == 1

def test_count_words_single_symbol():
    assert count_words('*') == 0

def test_count_words_invalid_type_raises_error():
    with pytest.raises(TypeError) as error_info:
        count_words(1)

    print(f"\nТекст ошибки: {error_info.value}")

    assert 'Функция работает только со строками' in str(error_info.value)

print(test_count_words_invalid_type_raises_error())