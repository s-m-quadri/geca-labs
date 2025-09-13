
def fractional_knapsack(capacity, items):
    # Step 1: Sort items by value-to-weight ratio (descending)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    for value, weight in items:
        if capacity == 0:
            break
        if weight <= capacity:
            # Take the whole item
            total_value += value
            capacity -= weight
        else:
            # Take a fraction of the item
            fraction = capacity / weight
            total_value += value * fraction
            capacity = 0  # knapsack is full

    return total_value


# Example usage:
capacity = 50
items = [(60, 10), (100, 20), (120, 30)]
print("Maximum value:", fractional_knapsack(capacity, items))  # Output: 240.0
