#include <stdio.h>
#include <limits.h>
#include <stddef.h>
#include <stdlib.h>

int max_array(const int array[], size_t size)
{
    if (array == NULL)
    {
        return (INT_MIN);
    }

    int max_value = array[0];

    size_t i = 1;

    while (i < size)
    {
        if (array[i] > max_value)
        {
            max_value = array[i];
        }
        i++;
    }

    return max_value;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        return (0);
    }

    int nbr[argc - 1];
    int i = 1;

    while (i < argc)
    {
        nbr[i - 1] = atoi(argv[i]);
        i++;
    }
    
    int max_value = max_array(nbr, argc - 1);
    printf("The max value is : %d\n", max_value);

    return (0);
}
