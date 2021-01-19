from time import sleep


class TrafficLight:
    __color = "red"

    def run(self):
        print(self.__color)
        sleep(TrafficLight.COLORS_DURATION.get(self.__color))
        if self.__color == "red":
            self.__color = "yellow"
        elif self.__color == "yellow":
            self.__color = "green"
        else:
            self.__color = "red"

    COLORS_DURATION: dict = {"red": 7, "yellow": 2, "green": 5}


trafficLight = TrafficLight()
for _ in range(10):
    trafficLight.run()
