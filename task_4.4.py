# Task 4.4: Fractional Knapsack
# ---------------------------
# Implement the greedy algorithm for the Fractional Knapsack problem.
# Steps:
# 1. Define items with (value, weight).
# 2. Sort items by value-to-weight ratio.
# 3. Add items fully until the knapsack is full.
# 4. If capacity is left, add fraction of next item.


#solution
def fractional_knapsack(capacity, items):
    """
    Compute maximum value achievable in a fractional knapsack.

    Parameters:
        capacity (float): Maximum weight the knapsack can carry
        items (list of tuples): Each tuple is (value, weight)

    Returns:
        float: Maximum achievable value
    """
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0.0
    for value, weight in items:
        if capacity >= weight:
            # Take wholeeeee
            capacity -= weight
            total_value += value
        else:
            # or just take fraction
            total_value += value * (capacity / weight)
            break  # Knapsack is fulllllllll
    return total_value

# Example (very important)
capacity1 = 50
items1 = [(60,10), (100,20), (120,30)]
print("Example 1 - Maximum value:", fractional_knapsack(capacity1, items1))  


capacity2 = 15  
items2 = [(500,5), (300,4), (400,6)]
print("Example 2 - Maximum value:", fractional_knapsack(capacity2, items2))  


capacity3 = 10  
items3 = [(200,5), (180,4), (120,3)]
print("Example 3 - Maximum value:", fractional_knapsack(capacity3, items3))  
