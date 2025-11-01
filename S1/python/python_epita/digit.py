def digit(n: int, k: int) -> int:

    i = 0

    if n <= 0 or k <= 0:
        return 0

    tpr = str(n)

    if k > len(tpr):
        return 0
    else:
        return int(tpr[len(tpr) - k])
