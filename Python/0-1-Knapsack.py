#The popular 0-1 Knapsack Problem

#Solution:


def knapsack(items, capacity):
    # Initialize a table to store the maximum values for each subproblem.
    # Table dimensions are (number of items + 1) x (capacity + 1).
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill in the table using dynamic programming.
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight exceeds the remaining capacity,
            # we can't include it in the knapsack.
            if items[i - 1][0] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # Otherwise, we have two choices: include the item or skip it.
                # We choose the maximum of these two values.
                included_value = items[i - 1][1] + dp[i - 1][w - items[i - 1][0]]
                excluded_value = dp[i - 1][w]
                dp[i][w] = max(included_value, excluded_value)

    # Now, dp[n][capacity] contains the maximum value that can be obtained.
    max_value = dp[n][capacity]

    # Backtrack to find the items included in the knapsack.
    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(items[i - 1])
            w -= items[i - 1][0]

    return max_value, included_items

# Get items and capacity from the user
items = []
num_items = int(input("Enter the number of items: "))
for i in range(num_items):
    weight = int(input(f"Enter the weight of item {i + 1}: "))
    value = int(input(f"Enter the value of item {i + 1}: "))
    items.append((weight, value))

capacity = int(input("Enter the knapsack capacity: "))

# Call the knapsack function
max_value, included_items = knapsack(items, capacity)
print("Maximum value:", max_value)
print("Included items:", included_items)
