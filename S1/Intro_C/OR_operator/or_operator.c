#include <stdio.h>

int main(void)
{
    unsigned int a = 1;
    unsigned int b = 0;
    //this will be 1
    unsigned char a_or_b = a | b;

    printf("RESULT: %d\n", a_or_b);

    return 0;
}
