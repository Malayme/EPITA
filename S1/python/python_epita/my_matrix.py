def is_matrix(parameter: list[list[float]]) -> bool :

    if not isinstance(parameter, list) or not parameter:
        return False
    row_len = len(parameter[0])
    for row in parameter:
        if not isinstance(row, list) or len(row) != row_len:
            return False
    return True

def print_matrix(parameter: list[list[float]]) -> None :

    if is_matrix(parameter):
        for row in parameter:
            print(" ".join(map(str, row)))
    else:
        print("not a matrix")

def row_count(matrix: list[list[float]]) -> int :

    if is_matrix(matrix):
        return len(matrix)
    return None

def column_count(matrix: list[list[float]]) -> int :

    if is_matrix(matrix):
        return len(matrix[0])
    return None

def size(matrix: list[list[float]]) -> int :

     if is_matrix(matrix):
         return row_count(matrix)*column_count(matrix)
     return None

def are_equal(matrix1: list[list[float]], matrix2: list[list[float]]) -> bool:

    if  is_matrix(matrix1) and not is_matrix(matrix2):
        return None
    if  is_matrix(matrix2) and not is_matrix(matrix1):
        return None
    if is_matrix(matrix1) and is_matrix(matrix2):
        return matrix1 == matrix2
    return False

def is_square(matrix: list[list[float]]) -> bool:

    if is_matrix(matrix):
        return row_count(matrix) == column_count(matrix)
    else:
        return None
    return False

def is_identity(matrix: list[list[float]]) -> bool:

    if is_square(matrix):
        size = row_count(matrix)

        for i in range(size):
            for j in range(size):
                if i == j and matrix[i][j] != 1:
                    return False
                elif i != j and matrix[i][j] != 0:
                    return False

        return True

    return False

def is_diagonal(matrix: list[list[float]]) -> bool:

    if is_square(matrix):
        size = row_count(matrix)

        for i in range(size):
            for j in range(size):
                if i != j and matrix[i][j] != 0:
                    return False

        return True
    return False

def is_symmetric(matrix: list[list[float]]) -> bool:

    if is_square(matrix):
        size = row_count(matrix)

        for i in range(size):
            for j in range(size):
                if matrix[i][j] != matrix[j][i]:
                    return False

        return True
    return False

def is_triangular(matrix: list[list[float]]) -> bool:

    if is_square(matrix):
        size = row_count(matrix)

        for i in range(size):
            for j in range(i):
                if matrix[i][j] != 0 and matrix[j][i] != 0:
                    return False

        return True
    return False

def identity(n: int) -> list[list[float]]:

    if type(n) != int:
        return None
    if n < 0:
        return None
    if n == 0:
        return None
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def transpose(matrix: list[list[float]]) -> list[list[float]]:

    if is_matrix(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return None

def scalar_add(scalar: float, matrix: list[list[float]]) -> list[list[float]]:

    if is_matrix(matrix):
        return [[scalar + valeurs for valeurs in row] for row in matrix]
    return None

def scalar_multiply(scalar: float, matrix: list[list[float]]) -> list[list[float]]:

    if is_matrix(matrix):
        return [[scalar * valeur for valeur in row] for row in matrix]
    return None

def add(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:

    if is_matrix(matrix1) and is_matrix(matrix2) and size(matrix1) == size(matrix2):
        return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return None

def multiply(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:

    if size(matrix1) != size(matrix2):
        return None


    def size2(matrix: list[list[float]]) -> tuple:
        return len(matrix), len(matrix[0])

    row1, column1 = size2(matrix1)
    row2, column2 = size2(matrix2)

    if column1 != row2:
        return None

    matrix3 = [[0.0 for cpt in range(column2)] for cpt in range(row1)]

    for i in range(row1):
        for j in range(column2):
            for k in range(column1):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]

    return matrix3


   # return [[matrix1[i][j] * matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def determinant(matrix: list[list[float]]) -> float:

         if len(matrix) == 2:
             return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
         else:
             return None

def is_invertible(matrix: list[list[float]]) -> bool:

  #  def determinant(matrix: list[list[float]]) -> float:

  #      if len(matrix) == 2:
  #          return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if is_matrix(matrix) == False:
        return None

    if is_square(matrix) and determinant(matrix) != 0:
        return True
    else:
        return False

    return False

def inverse(matrix: list[list[float]]) -> list[list[float]]:

    if is_invertible(matrix):
        n = determinant(matrix)
        return [[matrix[1][1] / n, -matrix[0][1] / n], [-matrix[1][0] / n, matrix[0][0] / n]]
    return None
























