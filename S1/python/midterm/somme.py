def somme(matriceA: list[list[float]], matriceB: list[list[float]]) -> list[list[float]]:

    if len(matriceA) != len(matriceB):
        return None
    return [[matriceA[i][j] + matriceB[i][j] for j in range(len(matriceA[0]))] for i in range(len(matriceA))]
