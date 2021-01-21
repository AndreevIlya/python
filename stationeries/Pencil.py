from stationeries.Stationery import Stationery


class Pencil(Stationery):
    title = "pencil"

    def draw(self):
        print(f"Drawing black and white pictures with a {self.title}")
