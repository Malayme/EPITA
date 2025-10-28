#include <stdio.h>

int main(void)
{
    int x = 42;
    int *ptr_x = &x;

    printf("Value of x : %d\n", x);
    printf("Address of x : %p\n", &x);
    printf("Value of ptr_x (address of x) : %p\n", ptr_x);
    printf("Value of ptr_x points to : %d\n", *ptr_x);

    return 0;
}
