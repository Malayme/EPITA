#include <stdio.h>

void do_the_magic(int *i, int *j)
{
    // *i-> Value: 42    Address: 0x48
    // *j-> Value: 51   Address: 0x4C
    // i ->     Value : 42 Address: Somewhere else in the memory
    // j ->     Value : 51 Adress: Somewhere else in the memory
    *i = 12;
    *j = 27;

    printf("*i: %d, *j: %d\n", *i, *j); // Prints "i : 12, j: 27"
}

int main(void)
{
    int foo = 42;   // Value: 42    Address : 0x48
    int bar = 51;   // Value: 51    Address : 0x4C

    printf("foo: %d, bar: %d\n", foo, bar); // prints "foo: 42, bar 51"
    do_the_magic(&foo, &bar);
    printf("foo: %d, bar : %d\n", foo, bar); // Prints "foo: 42, bar 51"
    
    return 0;
}



