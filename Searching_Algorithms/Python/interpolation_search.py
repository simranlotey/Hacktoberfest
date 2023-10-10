def interpolation_search(arr, target):
    """
    Perform interpolation search on the given sorted list.

    Parameters:
    - arr: The sorted list to search.
    - target: The element to search for.

    Returns:
    - index: The index of the target if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        mid = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
my_sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7
result = interpolation_search(my_sorted_list, target_value)
print(f"Interpolation Search: Target {target_value} {'found' if result != -1 else 'not found'} at index {result}")
