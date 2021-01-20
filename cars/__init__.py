from cars import Car
from cars.PoliceCar import PoliceCar
from cars.SportCar import SportCar
from cars.TownCar import TownCar
from cars.WorkCar import WorkCar

import random


def car_not_slower(car1: Car, car2: Car) -> str:
    return f"{car1.color} {car1.name} if not slower than {car2.color.lower()} {car2.name}. They'll never meet."


'''
    Second car tries to catch the first.
    If first car is slower they stop to decide what to do.
    If second car is police first car is inevitably arrested.
    Then they start moving with new paces.
    If first car is slower again they turn on a T cross.
    If they turn the same direction so first car is overtaken.
'''


def main():
    cars = [
        TownCar(name="Toyota", color="Red"),
        TownCar(name="Nissan", color="Green"),
        WorkCar(name="Ford", color="Blue"),
        WorkCar(name="Mini Cooper", color="White"),
        SportCar(name="Ferrari", color="Red"),
        SportCar(name="Maserati", color="Black"),
        PoliceCar(name="Dodge", color="Police")
    ]

    directions = ("left", "right")

    car1 = random.choice(cars)
    while True:
        car2 = random.choice(cars)
        if car2 != car1:
            break

    car1.go()
    car1.show_speed()
    car2.go()
    car2.show_speed()
    if car1.speed >= car2.speed:
        print(car_not_slower(car1, car2))
    else:
        car1.stop()
        car2.stop()
        if car2.is_police:
            print(f"{car1.color} {car1.name} is arrested!")
            return
        car1.go()
        car1.show_speed()
        car2.go()
        car2.show_speed()
        if car1.speed >= car2.speed:
            print(car_not_slower(car1, car2))
        else:
            car1_direction = random.choice(directions)
            car2_direction = random.choice(directions)
            car1.turn(car1_direction)
            car2.turn(car2_direction)
            if car1_direction == car2_direction:
                print(f"{car2.color} {car2.name} overtakes {car1.color.lower()} {car1.name}.")
            else:
                print(f"{car2.color} {car2.name} goes to the direction opposite to {car1.color.lower()} {car1.name}.")


if __name__ == '__main__':
    main()
