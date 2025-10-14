# Task 4.4: Fractional Knapsack
# ---------------------------
# Implement the greedy algorithm for the Fractional Knapsack problem.
# Steps:
# 1. Define items with (value, weight).
# 2. Sort items by value-to-weight ratio.
# 3. Add items fully until the knapsack is full.
# 4. If capacity is left, add fraction of next item.
#
# Input:
# - Capacity W
# - List of items (value, weight)
#
# Output:
# - Maximum achievable value
#
# Example:
# Capacity = 50
# Items = [(60,10), (100,20), (120,30)]
# Output: 240.0
#
# Hint: Use sorting and simple loops.
def fractional_knapsack(W, items):
    # Sort items by value-to-weight ratio (descending)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    for value, weight in items:
        if W == 0:
            break
        if weight <= W:
            total_value += value
            W -= weight
        else:
            fraction = W / weight
            total_value += value * fraction
            W = 0

    return total_value


# Example
capacity = 50
items = [(60, 10), (100, 20), (120, 30)]

print("Maximum value in Knapsack:", fractional_knapsack(capacity, items))
