import numpy as np

class UsefulMatrixMixin:
    def save_to_file(self, path):
        with open(path, 'w') as file:
            file.write(self.__str__() + '\n')

    def get_value(self, i, j):
        if (i > self.rows or i < 0 or j > self.cols or j < 0):
            raise ValueError("Index out of bounds")
        return self.matrix[i][j]
    
    def get_size(self):
        return (self.rows, self.cols)

    def set_value(self, i, j, value):
        if (i > self.rows or i < 0 or j > self.cols or j < 0):
            raise ValueError("Index out of bounds")
        self.matrix[i][j] = value

    def __str__(self):
        max_lengths = [max([len(str(row[i])) for row in self.matrix]) for i in range(self.cols)]

        table_str = ""
        for row in self.matrix:
            for i, element in enumerate(row):
                table_str += str(element).ljust(max_lengths[i]) + " "
            table_str += "\n"

        return table_str

class Matrix(UsefulMatrixMixin, np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        if not all(len(row) == self.cols for row in matrix):
            raise ValueError("All rows must have the same length")
        
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, (Matrix,)):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x.matrix if isinstance(x, Matrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.matrix if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

if __name__ == "__main__":
    np.random.seed(0)
    matrix1 = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix2 = Matrix(np.random.randint(0, 10, (10, 10)))
        
    res = matrix1 + matrix2
    res.save_to_file("./artifacts/3.2/matrix+.txt")

    res = matrix1 - matrix2
    res.save_to_file("./artifacts/3.2/matrix-.txt")
    
    res = matrix1 * matrix2
    res.save_to_file("./artifacts/3.2/matrix_mul.txt")
    
    res = matrix1 @ matrix2
    res.save_to_file("./artifacts/3.2/matrix@.txt")

    print("Size:")
    print(matrix1.get_size())
    print()

    print("Get value (5,5):")
    print(matrix1.get_value(5, 5))
    print()

    print("Set value (5,5) = 100:")
    matrix1.set_value(5, 5, 100)
    print(matrix1.get_value(5, 5))
    print()
    