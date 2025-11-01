#include <stdio.h>
#include <stdlib.h>

int min(int a, int b)
{
    if (a < b)
        return (a);
    else
        return (b);
}

int PGCD(int a, int b)
{
    int i = min(a, b);

    while (i > 0)
    {
        if((a % i == 0) && (b % i == 0))
        {
            printf("Le PGCD de %d et %d est %d", a, b, i);
            return (i);
        }
        i--;
    }
}

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("Usage: %s <nombre1> <nombre2>\n", argv[0]);
        return (1);
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    PGCD(a, b);
    
    return (0);

}