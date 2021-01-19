class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {}
