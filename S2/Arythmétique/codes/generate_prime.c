#include <stdio.h>
#include <stdlib.h>


int exposant(int phi)
{
    int e = phi + 1;
    printf("Your exposant = %d\n", e);

    return (0);
}

int phi_de_n(int phi_de_n)
{
    //e premier et inférieur avec Phi(n)

    return (0);
}

int ft_is_prime(int nb)
{
    int i = 1;

    if(nb < 2)
        return 0;
    while (++i <= nb / i)
    {
        if (nb % i == 0)
            return 0;
    }
    return 1;
}

int random_prime(int borneInf, int borneSup)
{
    int value = rand();

    printf("Your first random value is : %d\n", value);
    printf("Pass your random value in this inteval : 0 <= r modulo borneSup <= borneSup\n");

    int r = value % borneSup;

    printf("You obtained r = %d\n", r);
    printf("Is your r prime ? Verification...\n");

    if(ft_is_prime(r) != 1)
    {
        printf("\n You didn't obtained a prime value. Regenerate the program...\n");
    }
    else
    {
        printf("\nLaunch the calcul with Phi(n)...\n");
        //phi_de_n(r);
    }
    
    return (r);
}

int main(void)
{
    int borneInf = 10;
    int borneSup = 50;

    printf("Generate a random value between borneSup and borneInf...\n");
    random_prime(borneInf, borneSup);

    return 0;
}
