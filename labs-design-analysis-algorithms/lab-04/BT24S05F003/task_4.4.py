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
# fractional_knapsack.py
# Task 4.4: Fractional Knapsack Problem

def fractional_knapsack(capacity, items):
    """
    Solve the fractional knapsack problem using greedy approach.
    
    Parameters:
    - capacity: int, maximum weight the knapsack can hold
    - items: list of tuples, each tuple is (value, weight)
    
    Returns:
    - Maximum achievable value (float)
    """
    # Calculate value-to-weight ratio for each item
    items = [(value, weight, value/weight) for value, weight in items]
    
    # Sort items by decreasing value-to-weight ratio
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0
    for value, weight, ratio in items:
        if capacity == 0:
            break
        
        # Take full item if it fits
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            # Take fractional part
            total_value += ratio * capacity
            capacity = 0  # Knapsack is full
    
    return total_value


# Example usage
capacity = 50
items = [(60, 10), (100, 20), (120, 30)]
max_value = fractional_knapsack(capacity, items)
print(f"Maximum achievable value: {max_value}")  # Output: 240.0
