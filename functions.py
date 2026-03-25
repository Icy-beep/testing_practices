def calculate_sum(n: float) -> float:
    if isinstance(n, str):
        try:
            n = float(n)
        except ValueError:
            raise ValueError("невозможно преобразовать n в число")

    if n < 1:  raise ValueError("n не должен быть меньше 1")

    return n * (n + 1) / 2

f = calculate_sum(10)
print(f)


def count_words(line: str) -> int:
    if not isinstance(line, str):  raise TypeError('Функция работает только со строками')

    raw_words = line.split()

    clean_words = []
    for word in raw_words:
        if any(char.isalpha() for char in word):
            clean_words.append(word)

    return len(clean_words)

d = count_words('hello world, im a human and i destroy you')
print(d)


def is_number(string: str) -> bool:
    if not isinstance(string, str):
        return False
    try:
        int(string.strip())
        return True
    except ValueError:
        return False

f = '123 321'
print(is_number(f))


def unique(lst: list[str | int | float]) -> list[str | int | float]:
    if not isinstance(lst, list):  raise TypeError("Ожидался список")

    unique_lst = []
    unique_elements_find = False
    while not unique_elements_find:
        for element in lst:
            if element not in unique_lst:
                unique_lst.append(element)

        is_duplicate_found = False
        for i in range(len(unique_lst) - 1):
            if unique_lst[i] == unique_lst[i + 1]:
                is_duplicate_found = True
                break

        if not is_duplicate_found:
            unique_elements_find = True

    return unique_lst

f = [4.5, 2, 3, 3, '2', 'w', 'w', 'w']
print(unique(f))