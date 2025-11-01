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
        if ((a % i == 0) && (b % i == 0))
        {
            return (i);
        }
        i--;
    }
}

int inverseMod(int a, int b)
{
    if (PGCD(a, b) != 1)
    {
        printf("Les chiffres a et b ne sont pas premiers entre eux...\n");
        exit(EXIT_FAILURE);
    }
    int mod = b;
    int old_u = 1; //u0
    int u = 0; //u1
    int new_u = 0; //u2
    int q;
    int r = 0;

    while (r != 1)
    {
        r = a % b;
        q = a / b;
        new_u = old_u - q * u;
        old_u = u;
        u = new_u;
        a = b;
        b = r;
    }
    if( new_u < 0){
        return (new_u + mod);
    }
    return new_u;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("Veuillez mettre 2 valeurs appartenant à l'ensemble Z\n");
        exit(EXIT_FAILURE);
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    printf("Résultat: %d\n", inverseMod(a, b));

    return 0;
}
