#include <stdio.h>

int count_lines_file(FILE *file)
{
    int res = 1;
    char last = EOF;
    char current = fgetc(file);

    while(current != EOF)
    {
        if(last == '\n')
        {
            res++;
        }
        last = current;
        current = fgetc(file);
    }

    return res;
}
int count_lines(const char file_in)
{
    FILE *file = fopen("./file", "r");

    if (NULL == file)
    {
        return 1;
    }

    int res = count_lines_file(file);

    fclose(file);
    return res;
}

int main(void)
{
    printf("%d\n", count_lines("mon_fichier.txt"));

    return 0;
}
