def inserer(liste: list[float], index: int, valeur: float) -> list[float]:
    result = list[:]
    if index < 0:
        index = 0
    elif index >= len(liste):
        index = len(liste)
    result.insert(index, valeur)
    return result
