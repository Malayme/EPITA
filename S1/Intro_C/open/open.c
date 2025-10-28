#include <stdio.h>

int main(void)
{
    FILE *file = fopen("./test", "r+"); // Open a file in writting mode
                                    
    if (NULL == file)
    {
        puts("Could not open test file\n");
        return 1;
    }

    fprintf(file, "New Message\n"); // Write a message in the stream file

    fclose(file);

    return 0;
}
