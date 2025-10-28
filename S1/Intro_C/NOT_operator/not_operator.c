#include <stdio.h>

struct soo {
  int a : 1;
};

int main(void)
{
    struct soo a = {1};
    // this will be 0
    struct soo  not_a = {~a.a};
    
    printf("RESULT: %d\n", (int)not_a.a);
    return 0;
}
