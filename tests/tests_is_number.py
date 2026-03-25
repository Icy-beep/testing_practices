import pytest

from functions import is_number


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