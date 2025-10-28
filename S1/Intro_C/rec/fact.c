unsigned long fact(unsigned n)
{
    if (n == 0)
    {
        return (1);
    }
    return (n * fact(n - 1));
}

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if(argc != 2)
    {
        return (0);
    }
    unsigned long n = atoi(argv[1]);

    printf("fact(%lu) = %lu\n", n, fact(n));
    return (0);
}
