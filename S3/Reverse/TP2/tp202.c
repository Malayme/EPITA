#include <stdio.h>


int Mul(int c, int d){
    char buf[0x10]={0};
    return (c*d);
}


int main(void){
    int c = 3;
    int d = 7;
    int e = Mul(c, d);

    return e;
}
