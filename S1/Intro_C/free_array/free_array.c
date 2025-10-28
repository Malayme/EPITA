#include <stdio.h>
#include <stdlib.h>

void free_array(int *arr)
{
    if(NULL != arr)
    {
        free(arr);
    }
}

