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
# Task 4.4: Fractional Knapsack
# -----------------------------

def fractional_knapsack(capacity, items):
    # Step 1: Calculate value-to-weight ratio and sort items in descending order
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0  # Total value in the knapsack
    for value, weight in items:
        if capacity == 0:
            break  # Knapsack is full
        
        if weight <= capacity:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take the fractional part of the item
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0  # Knapsack is now full
    
    return total_value


# Example usage
capacity = 50
items = [(60, 10), (100, 20), (120, 30)]

max_value = fractional_knapsack(capacity, items)
print("Maximum achievable value:", max_value)
