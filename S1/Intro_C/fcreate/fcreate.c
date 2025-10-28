#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(void)
{
    FILE *file = fopen("./test", "w");
    fclose(file);

    chmod("./test", 0755);

    return 0;

}
