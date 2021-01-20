from cars.Car import Car


class SportCar(Car):

    @property
    def _min_speed(self) -> int:
        return 40

    @property
    def _max_speed(self) -> int:
        return 200

    @property
    def is_police(self):
        return False
