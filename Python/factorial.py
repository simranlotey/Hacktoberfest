def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Args:
        n (int): The non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of the input number.

    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    if n < 0:
        raise ValueError("Factorial is defined only for non-negative integers.")
    if n == 0 or n==1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(factorial(5))
