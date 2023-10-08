def merge_sort(arr):
    # Base case: If the array has only one element or is empty, it's already sorted.
    if len(arr) <= 1:
        return arr
    
    # Split the input array into two halves.
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]
    
    # Recursively sort each half.
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves back together.
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    # Compare elements from both halves and merge them in sorted order.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append any remaining elements from both halves (if any).
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)


# MERGE SORT

# Divide: First, it takes a big unsorted list and divides it into smaller sub-lists. It keeps doing this until each sub-list contains just one element. At this point, the individual elements are considered sorted by default because there's nothing to compare them to.

# Conquer: Then, it starts merging these smaller sub-lists back together in a sorted manner. It compares the elements in the sub-lists and puts them in the correct order while merging. It does this repeatedly until you end up with one single sorted list.

# The key idea behind merge sort is that it's easier to sort smaller lists and then combine them in a sorted way, rather than trying to sort the entire big list all at once.

# In simpler terms, you can think of it like sorting a deck of cards. First, you divide the deck into smaller piles, then you sort each pile separately (that's the "divide" step), and finally, you merge these sorted piles back together to get one sorted deck (that's the "conquer" step). This process ensures that the deck ends up sorted correctly.