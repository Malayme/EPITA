#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int miroir(int n)
{
    char c[50];
    int i;
    int j;
    int tpr;

    sprintf(c, "%d", n);

    for(i=0, j = strlen(c) - 1; i < j; i++, j--)
    {
        tpr = c[i];
        c[i] = c[j];
        c[j] = tpr;
    }
    return atoi(c);
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        return (0);
    }
    
    int n = atoi(argv[1]);
    int resultat = miroir(n);

    printf("Le miroir de %d, est %d\n", n, resultat);

    return (0);
}
