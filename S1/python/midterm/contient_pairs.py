def contient_pairs(liste: list[int]) -> bool:
    for number in liste:
        if number % 2 == 0:
            return True
    return False
