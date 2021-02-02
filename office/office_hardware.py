from abc import ABC, abstractmethod


class OfficeHardware(ABC):

    @property
    @abstractmethod
    def power(self) -> int:
        pass

    @property
    @abstractmethod
    def functionality(self) -> 'Functionality':
        pass

    @property
    def model(self) -> str:
        return self.__model

    def __init__(self, model: str):
        self.__model = model

    def __str__(self):
        return f"Power is {self.power} W.\nDevice functionality is {self.functionality}."


class Scanner(OfficeHardware):
    @property
    def power(self) -> int:
        return 50

    @property
    def functionality(self) -> 'Functionality':
        return Functionality(("scanning",))

    def __str__(self):
        return f"Scanner {self.model}.\n" + super().__str__() + "\n"


class Printer(OfficeHardware):
    @property
    def power(self) -> int:
        return 80

    @property
    def functionality(self) -> 'Functionality':
        return Functionality(("printing",))

    def __str__(self):
        return f"Printer {self.model}.\n" + super().__str__() + "\n"

    def __eq__(self, other):
        return self.model == other.model


class Xerox(OfficeHardware):
    @property
    def power(self) -> int:
        return 200

    @property
    def functionality(self) -> 'Functionality':
        return Functionality(("scanning", "printing", "copying"))

    def __str__(self):
        return f"Xerox {self.model}.\n" + super().__str__() + "\n"


class Functionality:
    __functions: tuple

    def __init__(self, functions: tuple):
        self.__functions = functions

    def __str__(self):
        string = ""
        for function in self.__functions:
            string += function
            string += ", "
        return string[: -2]
