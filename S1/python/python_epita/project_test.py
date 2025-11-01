def is_matrix(matrix):

    matrix = []

    if not isinstance(matrix, list) or len(matrix) == 0:
        return False

    if not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return False

    row_lenght = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list) or len(row) != row_lenght:
            return False

        return True

    column_lenght = matrix[[0 + 1]]

    for column in matrix:
        if not isinstance(column, list) or len(column) == column_lenght:
            return False

        return True

    def print_matrix(matrix):

        if is_matrix(matrix):
            for row in matrix:
                print(matrix)

        else:
            print("not a matrix")

    def row_count(matrix):

        i = 0

        for i in matrix:
            i += 1
        return i
