def fractional_knapsack(items, capacity):
    """
    items: list of tuples (value, weight)
    capacity: maximum weight of knapsack
    Returns: maximum value achievable (float)
    """
    # Calculate value-to-weight ratio and sort items by it (descending)
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    
    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            # Take whole item
            capacity -= weight
            total_value += value
        else:
            # Take fraction of the item
            fraction = capacity / weight
            total_value += value * fraction
            break  # Knapsack is full

    return total_value

# Test the function
W = int(input("Enter knapsack capacity: "))
n = int(input("Enter number of items: "))

items = []
for i in range(n):
    v = float(input(f"Enter value of item {i+1}: "))
    w = float(input(f"Enter weight of item {i+1}: "))
    items.append((v, w))

max_value = fractional_knapsack(items, W)
print(f"Maximum achievable value: {max_value}")
