def towers_of_hanoi(n: int) -> list[tuple[int, int]]:

   # src = 1
   # dst = 2
   # aux = 3

    def TowerOfHanoi(n , src, dst, aux, mvs):

        if n == 1:
            mvs.append((src, dst))
            return
        TowerOfHanoi(n-1, src, aux, dst, mvs)
        mvs.append((src, dst))
        TowerOfHanoi(n-1, aux, dst, src, mvs)

    mvs = []
    TowerOfHanoi(n, 1, 3, 2, mvs)
    #        return [(n, src, dst, aux)]

   # mvs = [TowerOfHanoi(n-1, src, aux, dst)]
   # mvs.append((src, dst))
   # mvs.append((n-1, aux, dst, src))

    return mvs
