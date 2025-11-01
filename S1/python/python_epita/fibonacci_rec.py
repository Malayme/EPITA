def fibonacci_rec(n: int) -> int:

    if (n <= 0):
        return (0)

    if (n <= 2):
        return (1)

    return (fibonacci_rec(n - 2) + fibonacci_rec(n - 1))
