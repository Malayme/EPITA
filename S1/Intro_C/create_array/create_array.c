#include <stdlib.h>
#include <stdio.h>

int *create_array(unsigned n)
{
    int *array = malloc(sizeof(int) * n);

    if(NULL == array)
    {
        puts("Error: malloc return NULL\n");
        return NULL;
    }

    return array;
}

