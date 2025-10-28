void infinite_recursion(void)
{
    infinite_recursion();
}

int main(void)
{
    infinite_recursion();
    return (0);
}
