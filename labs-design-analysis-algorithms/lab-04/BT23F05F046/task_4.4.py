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
def fractional_knapsack(capacity, items):
    # Step 1: Calculate value-to-weight ratio for each item
    items = [(value, weight, value/weight) for value, weight in items]
    
    # Step 2: Sort items by ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    
    # Step 3 & 4: Add items fully or partially
    for value, weight, ratio in items:
        if remaining_capacity >= weight:
            # Take full item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            total_value += value * (remaining_capacity / weight)
            break  # Knapsack is full
    
    return total_value

# Example usage
capacity = 50
items = [(60, 10), (100, 20), (120, 30)]
max_value = fractional_knapsack(capacity, items)
print("Maximum achievable value:", max_value)
