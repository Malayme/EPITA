def extraire(liste: list[float], debut: int, fin: int) -> list[float]:
    if debut < 0 or fin > len(liste) or debut >= fin:
        return None
    return liste[debut : fin]
