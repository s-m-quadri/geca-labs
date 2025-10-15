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
    """
    Solve fractional knapsack problem using greedy algorithm.
    
    Args:
        capacity: Maximum weight capacity of knapsack
        items: List of tuples (value, weight)
    
    Returns:
        tuple: (maximum_value, items_taken)
        items_taken is list of (value, weight, fraction_taken)
    """
    if capacity <= 0 or not items:
        return 0.0, []

    # Calculate value-to-weight ratio for each item and sort
    items_with_ratio = []
    for i, (value, weight) in enumerate(items):
        if weight > 0:  # Avoid division by zero
            ratio = value / weight
            items_with_ratio.append((ratio, value, weight, i))

    # Sort by value-to-weight ratio in descending order
    items_with_ratio.sort(reverse=True)

    total_value = 0.0
    remaining_capacity = capacity
    items_taken = []

    for ratio, value, weight, original_index in items_with_ratio:
        if remaining_capacity == 0:
            break

        if weight <= remaining_capacity:
            # Take the entire item
            total_value += value
            remaining_capacity -= weight
            items_taken.append((value, weight, 1.0))  # fraction = 1.0 (full item)
        else:
            # Take fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            items_taken.append((value, weight, fraction))
            remaining_capacity = 0

    return total_value, items_taken

def print_knapsack_solution(capacity, items, total_value, items_taken):
    """Print detailed solution of knapsack problem."""
    print(f"Knapsack Capacity: {capacity}")
    print(f"Items: {items}")
    print(f"Maximum Value: {total_value:.2f}")
    print("\nItems taken:")

    for i, (value, weight, fraction) in enumerate(items_taken):
        if fraction == 1.0:
            print(f"  Item {i+1}: Value={value}, Weight={weight}, Fraction=100%")
        else:
            print(f"  Item {i+1}: Value={value}, Weight={weight}, Fraction={fraction:.2%}")

if __name__ == "__main__":
    # Test case from the example
    capacity1 = 50
    items1 = [(60, 10), (100, 20), (120, 30)]

    print("Test Case 1:")
    print("=" * 40)
    total_value1, items_taken1 = fractional_knapsack(capacity1, items1)
    print_knapsack_solution(capacity1, items1, total_value1, items_taken1)
    print()

    # Additional test case
    capacity2 = 15
    items2 = [(10, 5), (40, 4), (30, 6), (50, 3)]

    print("Test Case 2:")
    print("=" * 40)
    total_value2, items_taken2 = fractional_knapsack(capacity2, items2)
    print_knapsack_solution(capacity2, items2, total_value2, items_taken2)