from datetime import datetime

class Temperature:
    __celsius: int

    ABS_ZERO_CELSIUS = -273
    PLANCK_TEMP_CELSIUS = 1.4168e32

    def __init__(self, celsius):
        if celsius < self.ABS_ZERO_CELSIUS:  raise ValueError("Температура не может быть ниже абсолютного нуля")
        if celsius > self.PLANCK_TEMP_CELSIUS:  raise ValueError("Температура не может быть выше Планковского предела")
        self.__celsius = celsius

    def __str__(self):
        if self.__celsius > 1e6:
            return f"{self.__celsius:e}°C"
        return f"{self.__celsius}°C"

    def get_value(self):
        return self.__celsius

    def to_fahrenheit(self):
        return (self.__celsius * (9 / 5)) + 32

    def to_kelvin(self):
        return self.__celsius + 273

    def is_positive(self):
        return self.__celsius > 0

    @staticmethod
    def compare(t1, t2):
        v1 = t1.get_value()
        v2 = t2.get_value()

        if v1 > v2:
            return -1
        elif v1 < v2:
            return 1
        else:
            return 0


t = Temperature(celsius=0)

print(Temperature.to_fahrenheit(t))

class LibraryBook:
    __title: str
    __author: str
    __publish_year: int

    def __init__(self, title, author, publish_year):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название книги должно быть непустой строкой")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Имя автора должно быть непустой строкой")

        current_system_year = datetime.now().year
        if not isinstance(publish_year, int) or publish_year > current_system_year:
            raise ValueError(f"Год издания ({publish_year}) не может быть больше текущего ({current_system_year})")

        self.__title = title
        self.__author = author
        self.__publish_year = publish_year

    def __str__(self):
        return f"Название книги: {self.__title}\nАвтор: {self.__author}\nГод выхода: {self.__publish_year}"

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publish_year(self):
        return self.__publish_year

    def rename(self, new_title):
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Новое название не может быть пустым")
        self.__title = new_title

    def age(self, current_year=None):
        if current_year is None:
            current_year = datetime.now().year

        if current_year < self.__publish_year:
            raise ValueError("Текущий год не может быть меньше года издания книги")

        return current_year - self.__publish_year

    def is_old(self, current_year=None):
        return self.age(current_year) > 50

book = LibraryBook("1984", "George Orwell", 1949)

print(book)

s = book.is_old()

print(s)

print(book.age())