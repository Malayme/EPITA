def int_palindrome(n: int) -> bool:
    if n < 0:
        return False

    string = str(n)
    inv_str = string[::-1]

    if inv_str == string:
        return True
    else:
        return False
