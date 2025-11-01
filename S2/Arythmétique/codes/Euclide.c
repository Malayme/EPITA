#include <stdio.h>
#include <stdlib.h>

int Euclide(int a, int b)
{
    int r = 1;

    while (r > 0)
    {
        r = a % b;
        a = b;
        b = r;
    }
    printf("Le PGCD est %d\n", a);
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: %s <a> <b>\n", argv[0]);
        return (1);
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    Euclide(a, b);

    return (0);
}
