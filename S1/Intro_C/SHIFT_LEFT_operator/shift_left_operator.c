#include <stdio.h>
//all commentaries int this file are not true

int main(void)
{
    unsigned char a = 1;
    //this will be 2
    // 00000001 << 1 = 00000010
    unsigned char b = a << 1;
    //this will be 4
    // 00000001 << 2 = 00000100
    unsigned char c = a << 2;

    printf("RESULT b : %d\n", b);
    printf("RESULT c : %d\n", c);

    return 0;

}
