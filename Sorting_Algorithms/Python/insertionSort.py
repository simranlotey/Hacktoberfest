"""
Insertion Sort is one of the simplest sorting techniques.
Its worst case time complexity is O(n^2).
However, its best case time complexity is O(n).
It is a stable algorithm, with an adaptive nature.

It is the algorithm with the lowest overhead.
The algorithm coded below has least number of swaps among the elementary sorting algorithms.

For higher overhead based scenarios, divide and conquer algorithms are used.
"""

def InsertionSort(array):
    # n stores the length of array we are trying to sort
    n = len(array)
    # Iterating through the array from the first position till the end
    for i in range(1,n):
        # Storing the location of current position
        position = i
        # Storing the value at the current position
        current_value = array[i]
        # Shifting the value backwards till it reaches its correct position relative to the
        # values to the left of current value
        while(position>0 and array[position-1]>current_value):
            array[position] = array[position-1]
            position = position - 1
        # Once the values are shifted right till we reach the desired location, 
        # The current value is stored in the "position" location
        array[position] = current_value
    # Return the sorted array
    return array