#include <stdio.h>
#include <stdlib.h>

#include "my_array.h"

struct my_array *array_create(size_t nb_elements)
{
    struct my_array* array = malloc(sizeof(struct my_array));

    if(NULL == array)
    {
        return NULL;
    }

    array->data = malloc(nb_elements * sizeof(int));
    array->size = nb_elements;

    if(array->data == NULL)
    {
        free(array);
        return NULL;
    }
    return array;

}

int main(void)
{
    struct my_array *my_array = array_create(42);
    void *data = my_array->data;

    if(NULL ==  my_array)
    {
        printf("No hero has been created\n");
    }
    else if (NULL == data)
    {
        printf("No pointer data has been created!\n");
    }
    else
    {
        printf("my-array has a size of %zu and my_array->data is %p.\n", my_array->size, data);
    }

    free(my_array);

    return 0;
}

