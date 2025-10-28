#include <stdio.h>

struct int_vector
{
    int size;
    int data[64];
};

int int_vector_min(struct int_vector *vec)
{
    int min = vec->data[0];
    int i = 1;

    while(i < vec->size)
    {
        if(vec->data[i] < min)
        {
            min = vec->data[i];
        }
        i++;
    }
    return min;
}

int int_vector_max(struct int_vector *vec)
{
    int max = vec->data[0];
    int i = 1;

    while(i < vec->size)
    {
        if(vec->data[i] > max)
        {
            max = vec->data[i];
        }
        i++;
    }
    return max;
}

int main(void)
{
    struct int_vector vec = {5, {1, 2, 3, 4, 5}};

    printf("min: %d\n", int_vector_min(&vec));
    printf("max: %d\n", int_vector_max(&vec));

    return 0;
}
