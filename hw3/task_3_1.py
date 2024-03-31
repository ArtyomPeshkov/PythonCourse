import numpy as np

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self._check_dimensions(matrix)

    def _check_dimensions(self, matrix):
        if not all(len(row) == self.cols for row in matrix):
            raise ValueError("All rows must have the same length")

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition")
        
        mat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            mat.append(row)

        return Matrix(mat)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for Adamar multiplication")
        
        mat = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] * other.matrix[i][j])
            mat.append(row)

        return Matrix(mat)
    
    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        
        mat = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                row.append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)))
            mat.append(row)

        return Matrix(mat)
    
    
    def __str__(self):
        max_lengths = [max([len(str(row[i])) for row in self.matrix]) for i in range(self.cols)]

        table_str = ""
        for row in self.matrix:
            for i, element in enumerate(row):
                table_str += str(element).ljust(max_lengths[i]) + " "
            table_str += "\n"

        return table_str


if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))

    print("\nMatrix1 + Matrix2:")
    print(matrix1 + matrix2)
    print()

    print("\nMatrix1 * Matrix2:")
    print(matrix1 * matrix2)
    print()

    print("\nMatrix1 @ Matrix2:")
    print(matrix1 @ matrix2)
    print()