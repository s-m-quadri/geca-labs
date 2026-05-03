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

# ---------------------------
# Task 4.4: Fractional Knapsack
# ---------------------------

# Function to calculate maximum value in Knapsack
def fractional_knapsack(values, weights, capacity):
    """Greedy algorithm for Fractional Knapsack."""
    
    # Step 1: Create a list of (value, weight, ratio)
    items = []
    for i in range(len(values)):
        ratio = values[i] / weights[i]
        items.append((values[i], weights[i], ratio))
    
    # Step 2: Sort items by value-to-weight ratio (descending order)
    items.sort(key=lambda x: x[2], reverse=True)
    
    total_value = 0.0  # Total value accumulated
    remaining_capacity = capacity  # Remaining weight capacity
    
    # Step 3 & 4: Add items (fully or fractionally)
    for value, weight, ratio in items:
        if remaining_capacity == 0:
            break
        
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the next item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
    
    return total_value


# Example usage:
values = [60, 100, 120]   # Item values
weights = [10, 20, 30]    # Item weights
capacity = 50             # Knapsack capacity

max_value = fractional_knapsack(values, weights, capacity)
print(f"Maximum value in the knapsack = {max_value:.2f}")
