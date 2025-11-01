#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    int x = 0;

    pid_t pid = fork();

    if(pid < 0)
    {
        return 1;
    }
    
    if(pid>0)
    {
        x++;
        printf("[Parebt] x: %d (%p)\n", x, &x);
    }else
        printf("[Child] x: %d (%p)\n", x, &x);

    return 0;

}
