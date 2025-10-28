/**
** \file my_array.h
*/

#ifndef MY_ARRAY_H
#define MY_ARRAY_H

#include <stddef.h>

struct my_array
{
    int *data;
    size_t size;
};

struct my_array *array_create(size_t nb_elements);

#endif /* ! MY_ARRAY_H */

