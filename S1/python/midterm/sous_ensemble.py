def sous_ensembles(ensemble: list[str]) -> list[list[str]]:

    if not ensemble:
        return [[]]
    element = ensemble[0]
    subsets = sous_ensembles[1:]
    return subsets + [subset + [element] for subset in subsets]
