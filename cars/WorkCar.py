from cars.Car import Car


class WorkCar(Car):

    @property
    def _min_speed(self) -> int:
        return 20

    @property
    def _max_speed(self) -> int:
        return 60

    @property
    def is_police(self):
        return False

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"Car {self.name} speeds too fast!")
