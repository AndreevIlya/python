class ZeroDivisionException(Exception):
    def __init__(self, numerator: float, denominator: float):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"Division by zero encountered in {self.numerator} / {self.denominator}."


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionException(a, b)
    return a / b


try:
    divide(1, 0)
except ZeroDivisionException as exc:
    print(exc)
