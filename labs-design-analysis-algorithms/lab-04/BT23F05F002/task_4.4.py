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
    items_with_ratio = []
    for i, (value, weight) in enumerate(items):
        ratio = value / weight
        items_with_ratio.append((ratio, value, weight, i))
    
    items_with_ratio.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    current_weight = 0
    selected_items = []
    
    for ratio, value, weight, original_index in items_with_ratio:
        if current_weight + weight <= capacity:
            total_value += value
            current_weight += weight
            selected_items.append((original_index, 1.0, value))
        else:
            remaining_capacity = capacity - current_weight
            if remaining_capacity > 0:
                fraction = remaining_capacity / weight
                total_value += value * fraction
                current_weight += remaining_capacity
                selected_items.append((original_index, fraction, value * fraction))
            break
    
    return total_value, selected_items

def print_knapsack_solution(capacity, items, total_value, selected_items):
    print(f"Knapsack Capacity: {capacity}")
    print("Items: (value, weight)")
    for i, (value, weight) in enumerate(items):
        print(f"  Item {i}: ({value}, {weight}) - ratio: {value/weight:.2f}")
    
    print(f"\nMaximum value: {total_value:.1f}")
    print("Selected items:")
    for item_index, fraction, value_taken in selected_items:
        value, weight = items[item_index]
        if fraction == 1.0:
            print(f"  Item {item_index}: Full item - value: {value_taken:.1f}")
        else:
            print(f"  Item {item_index}: {fraction:.2f} fraction - value: {value_taken:.1f}")

capacity = 50
items = [(60, 10), (100, 20), (120, 30)]
total_value, selected_items = fractional_knapsack(capacity, items)
print_knapsack_solution(capacity, items, total_value, selected_items)

print("\n" + "="*50)

capacity2 = 15
items2 = [(10, 5), (40, 4), (30, 6), (50, 3)]
total_value2, selected_items2 = fractional_knapsack(capacity2, items2)
print_knapsack_solution(capacity2, items2, total_value2, selected_items2)
