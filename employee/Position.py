from random import randrange

from employee.Worker import Worker


class Position(Worker):

    def __init__(self, name: str, surname: str, position: str):
        super().__init__(name, surname, position)
        self._income["wage"] = randrange(5, 20) * 100
        self._income["bonus"] = randrange(50, 100) * self._income["wage"] / 100

    def get_full_name(self) -> str:
        return f"{self.position} {self.name} {self.surname}"

    def get_total_income(self, months_count: int) -> int:
        return self._income["wage"] * months_count + months_count // 12 * self._income["bonus"]


worker1 = Position("John", "Henderson", "Python developer")
worker2 = Position("Alex", "Blackthorn", "Android developer")
print(f"{worker1.get_full_name()} has income per 24 months {worker1.get_total_income(24)} $")
print(f"{worker2.get_full_name()} has income per 24 months {worker2.get_total_income(24)} $")
