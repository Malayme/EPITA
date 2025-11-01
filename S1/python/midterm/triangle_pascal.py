def triangle_pascal(ordre: int) -> list[list[int]]:

    if ordre < 0:
        return None
    triangle = [[1]]
    for i in range (1, ordre + 1):
        row = [i]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
