#include <stdio.h>

int main(void)
{
    unsigned char a = 4;
    //this will be 2
    // 00000100 >> 1 = 00000010
    unsigned char b = a >> 1;
    // this will be 1
    // 00000100 >> 2 = 00000001
    unsigned char c = a >> 2;

    printf("RESULT b : %d\n", b);
    printf("RESULT c : %d\n", c);

    return 0;
}
