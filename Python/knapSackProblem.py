def knapsack_problem(items, capacity):
    knapsack_values = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        current_value, current_weight = items[i - 1]
        for c in range(capacity + 1):
            if current_weight > c:
                knapsack_values[i][c] = knapsack_values[i - 1][c]
            else:
                knapsack_values[i][c] = max(
                    knapsack_values[i - 1][c],
                    knapsack_values[i - 1][c - current_weight] + current_value
                )
    sequence = []
    i = len(items)
    c = capacity
    while i > 0:
        if knapsack_values[i][c] == knapsack_values[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    sequence.reverse()
    return [knapsack_values[len(items)][capacity], sequence]

items = [[1, 2], [4, 3], [5, 6], [6, 7]]
capacity = 10
result = knapsack_problem(items, capacity)
print("Maximum value:", result[0])
print("Items included:", result[1])