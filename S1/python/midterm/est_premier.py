def est_premier (entier: int) -> bool:
    if entier <= 1:
        return False
    for i in range(2, int(entier**0,5) + 1):
        if entier % i == 0:
            return False
    return True
