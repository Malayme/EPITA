def est_palindrome(chaine: str, debut: int, fin: int) -> bool:
    if debut >= fin:
        return True
    if chaine[debut] != chaine[fin - 1]:
        return False
    return est_palindrome(chaine, debut + 1, fin - 1)

