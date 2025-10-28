#include <stdio.h>

int main(void)
{
    int t = 8;

    if (t < 3)
    {
        printf("t < 3");
    }
    else if (3 <= t && t <= 6)
    {
        printf("3 <= t <= 6");
    }
    else
    {
        printf("t > 6");
    }

    return (0);
}
