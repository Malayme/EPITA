#include <stdio.h>

void reverse_print(char s[], int size)
{
    int i;
    i = size - 1;

    while (i >= 0)
    {
        printf("%c", s[i]);
        i--;
    }
}

int main(void)
{
    reverse_print("Hello World!", 12);
    puts("");
}

