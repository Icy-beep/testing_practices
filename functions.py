def calculate_sum(n: float) -> float:
    if isinstance(n, str):
        try:
            n = float(n)
        except ValueError:
            raise ValueError("невозможно преобразовать n в число")

    if n < 1:  raise ValueError("n не должен быть меньше 1")

    return n * (n + 1) / 2


f = calculate_sum(10**10)
print(f)

def count_words(line: str) -> int:
    if not isinstance(line, str):  raise TypeError('Функция работает только со строками')

    raw_words = line.split()

    clean_words = []
    for word in raw_words:
        if any(char.isalpha() for char in word):
            clean_words.append(word)

    return len(clean_words)


d = count_words('hello world')
print(d)