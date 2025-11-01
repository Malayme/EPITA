def inverse(entier: int, base: int) -> int:
    result = 0
    while entier > 0:
        result = result * base + entier % base
        entier //= base
    return result
