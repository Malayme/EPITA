#include <stdio.h>

int sum_n(unsigned n)
{
    unsigned int result = 0;

    while (n > 0)
    {
        result += n; 
        n--;
    }
    return (result);
}

int print_sum(int n)
{
    if (n < 0)
    {
        printf("Negative number !\n");
    }
    if (n >= 0)
    {
        printf("Result : %d\n", sum_n(n));
    }
    return (0);
}

int main(void)
{
    print_sum(-25);
    
    print_sum(0);
    
    print_sum(6);

    return (0);
}
