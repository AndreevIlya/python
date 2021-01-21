from stationeries.Stationery import Stationery


class Pen(Stationery):
    title = "pen"

    def draw(self):
        print(f"Writing with a {self.title}")
