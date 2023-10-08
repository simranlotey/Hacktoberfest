def linear_search(arr, target):
    """
    Perform a linear search to find the target element in a list.

    Args:
        arr (list): The list in which to search for the target.
        target: The element to search for.

    Returns:
        int: The index of the target element in the list if found, or -1 if not found.

    Examples:
        >>> linear_search([1, 2, 3, 4, 5], 3)
        2
        >>> linear_search([1, 2, 3, 4, 5], 6)
        -1
        >>> linear_search([], 3)
        -1
    """
    for index, item in enumerate(arr): # Iterate through whole array to find the element
        if item == target:
            return index  # Target found

    return -1  # Target not found in the list.

if __name__ == "__main__":
    import doctest
    doctest.testmod()