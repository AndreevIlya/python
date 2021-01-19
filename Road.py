class Road:
    __width: int  # m
    __length: int  # m
    __thickness: int  # cm

    def __init__(self, width: int, length: int, thickness: int):
        self.__width = width
        self.__length = length
        self.__thickness = thickness

    def calculate_asphalt_mass(self):
        return Road.__Asphalt.DENSITY * self.__width * self.__length * self.__thickness / 1000

    class __Asphalt:
        DENSITY = 25  # kg per 1 cm per 1 m2


print(f"For the road you need {Road(10, 500, 4).calculate_asphalt_mass()} tons of asphalt.")
