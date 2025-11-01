def fibonacci_iter(n: int) -> int:

    f0 = 0
    f1 = 1
    tpr = 0

    if n <= 0:
        return 0

    if n <= 2:
        return 1

    for i in range(n - 1):
        tpr = f1
        f1 = f1+f0
        f0 = tpr
    return f1
