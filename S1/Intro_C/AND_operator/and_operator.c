#include <stdio.h>

int main (void)
{
    unsigned char a = 1;
    unsigned char b = 0;
    //this will be 0
    unsigned char a_and_b = a & b;

    printf("a_and_b = %d\n", a_and_b);

    return 0;
}
