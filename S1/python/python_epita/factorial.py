def factorial(n :int) -> int:
    if n < 0:
        return (1)
    i = 1
    while n > 0:
        i *= n
        n -= 1
    return (i)
