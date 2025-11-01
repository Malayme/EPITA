def factorielle(entier: int) -> int:
    if entier == 0:
        return 1
    return entier * factorielle(entier - 1)
