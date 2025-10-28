#include <stdio.h>

void my_strupcase(char *str)
{
    int i;
    i = 0;

    while (str[i] != '\0')
    {
        if (str[i] >= 97 && str[i] <= 122)
        {
            str[i] -= 32;
        }
        i++;
    }
}

int main(void)
{
    char str[] = "azerty1234XYZ &C";
    my_strupcase(str);
    printf("%s\n", str);
    return 0;
}

