#include <stdio.h>

int main(void)
{
    puts("Please enter a character twice : ");
    char c1 = getchar();
    char c2 = getchar();
    puts("You pressed: ");
    putchar(c1);
    putchar(c2);
    putchar('\n');
    
    return (0);
}
