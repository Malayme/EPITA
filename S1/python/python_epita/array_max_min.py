def array_max_min(array: list[int]) -> tuple[int, int]:

   # maxi = array[0]
   # mini = array[0]

    if array == []:
        return (None, None)

    maxi = array[0]
    mini = array[0]

    for n in array:
        if n > maxi:
            maxi = n
        if n < mini:
            mini = n

    return (maxi, mini)
