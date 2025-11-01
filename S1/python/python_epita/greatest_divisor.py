def greatest_divisor(n :int) -> int:
    x = n - 1
    while x > 0:
        if n % x == 0:
            return x
        x -= 1
    return 1
