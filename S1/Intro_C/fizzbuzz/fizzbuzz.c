#include <stdio.h>

void fizzbuzz(unsigned int number)
{ // For each integer in [1, number]
    for (unsigned int n = 1; n <= number; ++n)
    {
        if (n % 3 == 0) 
            printf("Fizz");
        if (n % 5 == 0)
            printf("Buzz");
        // If n is a multiple of 15, the two above conditions print 'FizzBuzz'

        // If we do not print neither Fizz, Buzz nor FizzBuzz, print the number itself
        if (n % 3 != 0 && n % 5 != 0) printf("%u", n);

        // Add a separator between all numbers but not after the last one
        if (n < number) printf(", ");
    }
    putchar('\n');
}

int main(void)
{
    unsigned int number = 16;
    fizzbuzz(number);

    return 0;
}
