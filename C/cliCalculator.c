/**
 * Calculates the sum of two integers.
 *
 * @param a The first integer to be added.
 * @param b The second integer to be added.
 * @return The sum of the two integers.
 */

//Windows 

int sum(int a, int b) {
    return a + b;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
    if (argc == 4)
    {
        float a, b;
        a = atoi(argv[2]);
        b = atoi(argv[3]);

        if (strcmp(argv[1], "sum") == 0)
        {
            printf("Sum of %0.2f,%0.2f is %0.2f", a, b, a + b);
        }
        else if (strcmp(argv[1], "sub") == 0)
        {
            printf("Subtraction of %0.2f,%0.2f is %0.2f", a, b, a - b);
        }
        else if (strcmp(argv[1], "mul") == 0)
        {
            printf("Multiplication of %0.2f,%0.2f is %0.2f", a, b, a * b);
        }
        else if (strcmp(argv[1], "div") == 0)
        {
            printf("Division of %0.2f,%0.2f is %0.2f", a, b, a / b);
        }
	else
        {
            printf("****Wrong Format****\nUse:\n./[fileName].exe [sum/sub/mul/div] [Number1] [Number2]");
        }
    }
    else if (argc > 4)
    {
        printf("****Too many arguments supplied****\nUse:\n./[fileName].exe [sum/sub/mul/div] [Number1] [Number2]");
    }
    else
    {
        printf("****More arguments expected!!****\nUse:\n./[fileName].exe [sum/sub/mul/div] [Number1] [Number2]");
        return 0;
    }
    return 0;
}
