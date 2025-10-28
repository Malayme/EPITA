void weird_constness(const int *a, int * const b)
{
    *b = 1; // works well because the pointed value of b is not const
    b = NULL; // generates a compilation error because b is const

    *a = 1; // generates a compiler error because the pointed value of a is const
    a = NULL; // works well because a is not const
}
