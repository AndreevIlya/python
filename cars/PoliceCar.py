from cars.Car import Car


class PoliceCar(Car):

    @property
    def _min_speed(self) -> int:
        return 20

    @property
    def _max_speed(self) -> int:
        return 140

    @property
    def is_police(self):
        return True
