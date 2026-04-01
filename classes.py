
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