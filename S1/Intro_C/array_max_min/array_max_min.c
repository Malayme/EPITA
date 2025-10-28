#include <stddef.h>
#include <stdio.h>

void array_max_min(int tab[], size_t len, int *max, int *min)
{
    if (tab == NULL)
    {
        return;
    }
    if (len == 0)
    {
        return;
    }

    size_t i;
    i = 0;
    
    while(i < len)
    {
        if (tab[i] > *max)
        {
            *max = tab[i];
        }
        if (tab[i] < *min)
        {
            *min = tab[i];
        }
        i++;
    }
}

int main(void)
{
    int max = 0;
    int min = 0;
    int tab[]= {5, 3, 1, 42, 53, 3, 47};
    size_t len = 7;

    array_max_min(tab, len, &max, &min);

    printf("max = %d\n", max);
    printf("min = %d\n", min);

    return (0);
}


