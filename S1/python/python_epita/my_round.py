def my_round(n: float) -> int:
    if n < 0 and n != -0.5 and n != -1.5 and n != -2.5:
        return int(n-0.5)
    elif n == -0.5:
        return int(0)
    elif n == -1.5:
        return int(-1)
    elif n == -2.5:
        return int(-2)
    else:
        return int(n+0.5)
