class HashMixin:
    def __hash__(self):
        # The sum of the matrix elements modulo a large prime number p
        p = (int(1e9) + 7)
        return sum(sum(row) % p for row in self.matrix) % p

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.matrix == other.matrix


class Matrix(HashMixin):
    _cache = {}
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
        
        hash_key = (hash(self),hash(other))
        if (hash_key in self._cache):
            return self._cache[hash_key]
        
        mat = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                row.append(sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.cols)))
            mat.append(row)

        self._cache[hash_key] = Matrix(mat)
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
    A = Matrix([[1,2],[3,4]])
    B = Matrix([[1,0],[0,1]])
    C = Matrix([[4,3],[2,1]])
    D = Matrix([[1,0],[0,1]])
    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)
    print("Matrix C:")
    print(C)
    print("Matrix D:")
    print(D)

    resAB = A @ B
    resCD = C @ D
    
    print("Matrix AB:")
    print(resAB)
    
    print("Matrix CD (cached):")
    print(resCD)


    print("Matrix AB hash:")
    print(hash(resAB))

    print("Matrix CD hash:")
    print(hash(resCD))
