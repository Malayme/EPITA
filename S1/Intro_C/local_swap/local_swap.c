#include <stdio.h>

void local_swap(int *pa, int *pb) 
{
    int tmp = *pa; 
    *pa = *pb;
    *pb = tmp;
}

int main(void)
{
    int a = 42;
    int b = 51;

    local_swap(&a, &b);   // Switch a and b value
    printf("%d %d\n", a, b);    // 51 42
    
    return (0);
}
