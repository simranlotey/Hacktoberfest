def fibonacci(n):
    """
    Generate the Fibonacci series up to the nth term.

    Args:
        n (int): The number of terms to generate in the Fibonacci series.

    Returns:
        list: A list containing the Fibonacci series up to the nth term.

    Examples:
        >>> fibonacci(0)
        []
        >>> fibonacci(1)
        [0]
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
        >>> fibonacci(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """

    if n <= 0:
        return []  # Return an empty list for n <= 0.
    elif n == 1:
        return [0]  # Return [0] for n = 1.

    fib_series = [0, 1]  # Initialize the Fibonacci series with the first two terms.

    while len(fib_series) < n:
        next_term = (
            fib_series[-1] + fib_series[-2]
        )  # Calculate the next Fibonacci term.
        fib_series.append(next_term)

    return fib_series


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(fibonacci(10))
