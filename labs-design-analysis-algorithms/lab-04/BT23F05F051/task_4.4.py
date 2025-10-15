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
# ---------------- Fractional Knapsack ----------------

def fractional_knapsack(items, capacity):
    """
    items: list of tuples (value, weight)
    capacity: maximum weight of knapsack
    Returns maximum achievable value
    """
    # Calculate value-to-weight ratio and sort items descending by ratio
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0.0  # Total value accumulated
    remaining_capacity = capacity

    for value, weight in items:
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            break  # Knapsack is full

    return total_value


# -------------------- Main Program --------------------
if __name__ == "__main__":
    W = float(input("Enter knapsack capacity: "))
    
    # Input items as comma-separated (value,weight)
    items_input = input("Enter items as value,weight pairs separated by space (e.g., 60,10 100,20 120,30): ")
    
    # Parse items
    items = []
    for pair in items_input.split():
        value, weight = pair.split(",")
        items.append((float(value), float(weight)))

    max_value = fractional_knapsack(items, W)
    print(f"Maximum achievable value: {max_value}")
