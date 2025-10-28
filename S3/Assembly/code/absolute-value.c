#include <stdio.h>
#include <stdlib.h>

long absoluye_value(long x, long y){
    if (x < 0){
        x = x * -1;
    }
    else if (y < 0){
        y = y * -1;
    }
    else{
        return x + y;
    }
    return x + y;
}

int main(){
    long x = -5;
    long y = 10;
    long result = absoluye_value(x, y);
    printf("The absolute value of %ld and %ld is: %ld\n", x, y, result);
    return 0;
}