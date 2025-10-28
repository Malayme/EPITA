#include <stdio.h>

struct complex
{
    int re;
    int im;
};

void print_complex(const struct complex *c) //function printing value of complex number
{
    printf("%d + i * %d\n", c->re, c->im);
}

struct add_complex(const struct complex *a, const struct complex *b)
{
    struct complex res = 
    {
        .re = a->re + b->re,
        .im = a->im + b->im
    };
    return res;
}

struct mul_complex(const struct complex *a, const struct complex *b)
{
    struct complex res =
    {
        .re = (a->re * b->re) - (a->im * b->im),
        .im = (a->re * b->im) + (a->im * b->re)
    };
    return res;
}

int main(void) 
{
    struct complex a = {.re = 3, .im = 5};
    struct complex b = {.re = -4, .im = 2};

    print_complex(&a);
    print_complex(&b);
    print_complex(add_complex(&a, &b));
    print_complex(mul_complex(&a, &b));
    
    return 0;
}
