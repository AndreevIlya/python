from stationeries.Stationery import Stationery


class Handle(Stationery):
    title = "handle"

    def draw(self):
        print(f"Drawing color pictures with a {self.title}")
