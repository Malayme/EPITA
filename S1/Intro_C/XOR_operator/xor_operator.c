#include <stdio.h>

int main(void)
{
    unsigned char a = 1;
    unsigned char b = 0;
    // this will be 1
    unsigned char a_xor_b = a ^ b;
    // this will be 0
    unsigned char a_xor_1 = a ^ 1;

    printf("Result a_xor_b : %d\n", a_xor_b);
    printf("Result a_xor_1 : %d\n", a_xor_1);

    return 0;
}
