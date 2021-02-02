class ComplexNumber:
    __a: float
    __b: float

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    def __init__(self, a: float, b: float):
        self.__a = a
        self.__b = b

    def __add__(self, other):
        return ComplexNumber(self.__a + other.a, self.__b + other.b)

    def __sub__(self, other):
        return ComplexNumber(self.__a - other.a, self.__b - other.b)

    def __mul__(self, other):
        return ComplexNumber(self.__a * other.a - self.__b * other.b, self.__a * other.b + self.__b * other.a)

    def __truediv__(self, other):
        denominator = other.a * other.a + other.b * other.b
        real = (self.__a * other.a + self.__b * other.b) / denominator
        imaginary = (self.__b * other.a - self.__a * other.b) / denominator
        return ComplexNumber(real, imaginary)

    def __str__(self):
        if self.__a == 0 and self.__b == 0:
            return "0"
        if self.__a == 0:
            return f"{self.__b}i"
        if self.__b == 0:
            return f"{self.__a}"
        if self.__b == 1:
            return f"{self.__a} + i"
        if self.__b == -1:
            return f"{self.__a} - i"
        if self.__b > 0:
            return f"{self.__a} + {abs(self.__b)}i"
        if self.__b < 0:
            return f"{self.__a} - {abs(self.__b)}i"


num1 = ComplexNumber(1, 1)
num2 = ComplexNumber(1, -1)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
