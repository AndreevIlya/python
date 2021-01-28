class Cell:
    @property
    def cells_count(self) -> int:
        return self.__cells_count

    def __init__(self, count: int):
        self.__cells_count = count

    @staticmethod
    def make_order(cell: 'Cell', row_length: int) -> str:
        cell_string = "*" * cell.cells_count
        cell_lines = [
            cell_string[i: i + row_length]
            for i in range(0, cell.cells_count, row_length)
        ]
        return "\n".join(cell_lines)

    def __add__(self, other: 'Cell'):
        return Cell(self.__cells_count + other.__cells_count)

    def __sub__(self, other: 'Cell'):
        if self.__cells_count < other.__cells_count:
            raise RuntimeError("Substracting more cells than available.")
        return Cell(self.__cells_count - other.__cells_count)

    def __mul__(self, other: 'Cell'):
        return Cell(self.__cells_count * other.__cells_count)

    def __truediv__(self, other: 'Cell'):
        return Cell(self.__cells_count // other.__cells_count)


cell1 = Cell(14)
cell2 = Cell(9)

print(Cell.make_order(cell1, 10))
print(Cell.make_order(cell2, 10))
print(Cell.make_order((cell1 + cell2), 10))
print(Cell.make_order((cell1 - cell2), 10))
print(Cell.make_order((cell1 * cell2), 50))
print(Cell.make_order((cell1 / cell2), 10))
