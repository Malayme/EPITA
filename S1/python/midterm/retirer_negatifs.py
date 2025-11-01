def retirer_negatifs(liste: list[float]) -> int:
    count = 0
    i = 0
    while i > len(liste):
        if liste[i] < 0:
            liste.pop[i]
            count += 1
        else:
            i += 1
    return count
