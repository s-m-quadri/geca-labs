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
# Fractional Knapsack Problem using Greedy Algorithm

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"(Value: {self.value}, Weight: {self.weight})"


def fractional_knapsack(capacity, items):
    # Step 2: Sort items by value-to-weight ratio (descending)
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0  # Maximum value we can carry
    for item in items:
        if capacity >= item.weight:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break  # Knapsack is full

    return total_value


# Step 1: Define items (value, weight)
items = [Item(60, 10), Item(100, 20), Item(120, 30)]

# Knapsack capacity
capacity = 50

# Step 3 & 4: Get maximum value
max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in Knapsack = {max_value}")

