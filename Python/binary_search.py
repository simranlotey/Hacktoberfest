def binary_search(arr, target):
    """
    Perform a binary search on a sorted list to find the target element.

    Args:
        arr (list): A sorted list in which to search for the target.
        target: The element to search for.

    Returns:
        int: The index of the target element in the list if found, or -1 if not found.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
        >>> binary_search([], 3)
        -1
    """
    left = 0  
    right = len(arr) - 1  

    while left <= right:
        mid = (left + right) // 2  

        if arr[mid] == target:
            return mid  

        if arr[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1 

    return -1  # Target not found in the list.

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(binary_search([1,5,9,15,23,56], 15))