#include <stdio.h>

int	is_factorial(int	n)
{
	unsigned int	result;

	result = 1;
	while (n > 0)
	{
		result *= n;
		n--;
	}
	if (n < 0)
	{
		return (0);
	}
	return (result);
}

int main (void)
{
	printf("%d", is_factorial(10));
}
