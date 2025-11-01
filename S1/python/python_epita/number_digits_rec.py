def number_digits_rec(n: int) -> int:
    if n < 10:
        return 1
    else:
        return 1 + number_digits_rec( n // 10 )
