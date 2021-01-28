from random import randrange


class Matrix:
    __rows_count: int
    __columns_count: int
    __matrix: list

    def __init__(self, list_of_lists: list):
        self.__rows_count = len(list_of_lists)
        self.__columns_count = 0
        self.__matrix = []
        for row in list_of_lists:
            if not isinstance(row, list):
                raise RuntimeError("Row is not a list!")
            row = list(row)
            if self.__columns_count == 0:
                self.__columns_count = len(row)
            else:
                if self.__columns_count != len(row):
                    raise RuntimeError("Rows lengths don't match!")
            for item in row:
                if not isinstance(item, int):
                    raise RuntimeError("Nan is input!")
            self.__matrix.append(row)

    def __str__(self):
        matrix_string = ""
        for row in self.__matrix:
            matrix_string += "( "
            for item in row:
                matrix_string += str(item) + " "
            matrix_string += ")\n"
        return matrix_string

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise RuntimeError("You try to add not a matrix!")
        if self.__columns_count != other.__columns_count or self.__rows_count != other.__rows_count:
            raise RuntimeError("Columns or rows count don't match!")
        return Matrix([
            [self.__matrix[j][i] + other.__matrix[j][i] for i in range(self.__columns_count)]
            for j in range(self.__rows_count)])


rows = randrange(1, 11)
columns = randrange(1, 11)

matrix1 = Matrix([[randrange(1, 100) for _ in range(columns)] for _ in range(rows)])
matrix2 = Matrix([[randrange(1, 100) for _ in range(columns)] for _ in range(rows)])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
