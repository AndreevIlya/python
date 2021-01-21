from stationeries.Handle import Handle
from stationeries.Pen import Pen
from stationeries.Pencil import Pencil


def main():
    for stationery in [Pen(), Pencil(), Handle()]:
        stationery.draw()


if __name__ == '__main__':
    main()
