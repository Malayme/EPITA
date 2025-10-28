#include <stdlib.h>
#include <stdio.h>

int *create_my_int_array(size_t size)
{
    int *array = malloc(size * 4); // nombre d'éléments * la taille d'un élément

    if (NULL == array) //return value of malloc
    {
        puts("Error(create_my_int_array): malloc returned NULL\n");
        return NULL;
    }

    for(size_t i = 0; i < size; i++)
    {
        array[i] = i;
    }

    return array;
}

int main(void)
{
    size_t size = 10;
    int *ptr = create_my_int_array(size);

    if(NULL == ptr)
    {
        puts("Error(main): malloc returned Null\n");
        return 1;
    }

    for(size_t i = 0; i < size; i++)
    {
        printf("%d\n", ptr[i]);
    }

    free(ptr);
    return 0;
}



