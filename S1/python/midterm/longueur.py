def longueur(entier: int, base: int) -> int:
    count = 0
    while entier > 0:
        entier //= base
        count += 1
    return count if count > 0 else 1
