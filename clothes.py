from abc import ABC, abstractmethod


class Clothes(ABC):

    @property
    @abstractmethod
    def amount_of_cloth(self) -> float:
        pass


class Coat(Clothes):
    def __init__(self, size: float):
        self.__size = size

    @property
    def amount_of_cloth(self) -> float:
        return self.__size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height: float):
        self.__height = height

    @property
    def amount_of_cloth(self) -> float:
        return 2 * self.__height + 0.3


for item in [Coat(26), Coat(52), Suit(12), Suit(21)]:
    print(item.amount_of_cloth)
