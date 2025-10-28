#include <stdlib.h>
#include <stdio.h>

char *strupcase_dup(char *s, size_t size)
{
    char *new_s = malloc((size + 1) * sizeof(char));

    if(NULL == new_s)
    {
        puts("Error: malloc returned NULL\n");
        return NULL;
    }

    for(size_t i = 0; s[i] != '\0'; i++)
    {
        if(s[i] >= 'a' && s[i] <= 'z')
        {
            new_s[i] = s[i] - 'a' + 'A';
        }
        else
        {
            new_s[i] = s[i];
        }
    }
    new_s[size] = 0;
    return new_s;
}

int main(void)
{
    char s[] = "Hello, World!";
    size_t size = 14;
    char *new_s = strupcase_dup(s, size);
    
    if(NULL == new_s)
    {
        puts("Error (main): strupcase_dup (malloc) returned NULL\n");
        return 1;
    }

    for(size_t i = 0; i < size; i++)
    {
        printf("%c", new_s[i]);
    }

    return 0;

}


