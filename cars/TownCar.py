from cars.Car import Car


class TownCar(Car):
    @property
    def _min_speed(self):
        return 20

    @property
    def _max_speed(self):
        return 90

    @property
    def is_police(self):
        return False

    def show_speed(self):
        super(TownCar, self).show_speed()
        if self.speed > 60:
            print(f"Car {self.name} speeds too fast!")
