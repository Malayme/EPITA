def my_power1(num: int, n:int) -> int:
    return (num ** n)
def my_power2(num: int, n:int) -> int:
    i = 1
    for tpr in range(n):
        i *= num
    return i
def my_power3(num: int, n:int) -> int:
    if n == 0:
        return 1
    return num * my_power3(num, n - 1)
