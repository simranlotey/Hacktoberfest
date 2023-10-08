def bubble_sort(arr):
    # Get the length of the input array.
    n = len(arr)

    # Traverse through all elements in the array.
    for i in range(n):
        # Flag to check if any swapping occurs in this pass.
        swapped = False

        # Last i elements are already in place, so we don't need to check them again.
        for j in range(0, n-i-1):
            # If the current element is greater than the next element, swap them.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the array is already sorted.
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)


# BUBBLE SORT

# one of the simplest sorting algorithms

# time complex - O(n^2)

# Bubble sort is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, indicating that the list is sorted.