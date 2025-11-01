def Eratosthène(n):
    primes = [True] * (n+1)
    p=2
    while (p*p <= n):
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1
    return primes

n = int(input("Entrez un nombre: "))
print(Eratosthène(n))
