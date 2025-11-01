def min(liste: list[float]) -> float:

    smallest = float('inf')
    for value in liste:
        if value < smallest:
            smallest = value
    return smallest
