#include <iostream>

void fibonacci(int n)
{
    int a = 0, b = 1, next;
    std::cout << "Fibonacci Series: ";
    for (int i = 0; i < n; ++i)
    {
        std::cout << a << " ";
        next = a + b;
        a = b;
        b = next;
    }
    std::cout << std::endl;
}

int main()
{
    int n;
    std::cout << "Enter the number of terms: ";
    std::cin >> n;
    fibonacci(n);
    return 0;
}
