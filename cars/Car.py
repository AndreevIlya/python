from random import randrange

from abc import ABC, abstractmethod


class Car(ABC):
    speed: int
    color: str
    name: str

    @property
    @abstractmethod
    def _min_speed(self) -> int:
        pass

    @_min_speed.setter
    @abstractmethod
    def _min_speed(self, value):
        pass

    @property
    @abstractmethod
    def _max_speed(self) -> int:
        pass

    @_max_speed.setter
    @abstractmethod
    def _max_speed(self, value):
        pass

    @property
    @abstractmethod
    def is_police(self) -> bool:
        pass

    @is_police.setter
    @abstractmethod
    def is_police(self, value):
        pass

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color
        self.speed = randrange(self._min_speed, self._max_speed)

    def go(self):
        print(f"Car {self.name} color {self.color} goes.")
        if self.speed == 0:
            self.speed = randrange(self._min_speed, self._max_speed)

    def stop(self):
        print(f"Car {self.name} color {self.color} stops.")
        self.speed = 0

    def turn(self, direction: str):
        print(f"Car {self.name} color {self.color} turns to {direction}")

    def show_speed(self):
        print(f"{self.name}'s speed is {self.speed}")

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color
