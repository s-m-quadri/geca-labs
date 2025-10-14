def fractional_knapsack(capacity, items):
    """
    items: list of tuples (value, weight)
    capacity: maximum weight knapsack can hold
    returns: maximum achievable value (float)
    """
    # Step 1: Compute value-to-weight ratio and sort items (descending)
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0  # total profit in knapsack
    remaining_capacity = capacity

    # Step 2: Iterate through sorted items
    for value, weight in items:
        if remaining_capacity == 0:
            break

        # If the whole item fits, take it fully
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the remaining capacity
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0  # knapsack now full

    return total_value


# Example usage
capacity = 50
items = [(60, 10), (100, 20), (120, 30)]
print("Maximum value in Knapsack =", fractional_knapsack(capacity, items))
# Output: 240.0
