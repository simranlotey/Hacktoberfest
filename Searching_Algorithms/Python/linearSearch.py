def linear_search(arr, target):
    # Iterate through the array element by element.
    for i in range(len(arr)):
        # If the current element is equal to the target, return its index.
        if arr[i] == target:
            return i
    
    # If the target is not found in the array, return -1 to indicate it's not present.
    return -1

# Example usage:
arr = [68, 33, 25, 15, 22, 11, 80]
target = 25
result = linear_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
