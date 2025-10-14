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
	"""Return the maximum achievable value for the fractional knapsack problem."""
	# Sort items by value-to-weight ratio in descending order
	items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
	total_value = 0.0
	for value, weight in items:
		if capacity == 0:
			break
		if weight <= capacity:
			total_value += value
			capacity -= weight
		else:
			total_value += value * (capacity / weight)
			capacity = 0
	return total_value

if __name__ == "__main__":
	W = float(input("Enter knapsack capacity: "))
	n = int(input("Enter number of items: "))
	items = []
	for i in range(n):
		v = float(input(f"Enter value of item {i+1}: "))
		w = float(input(f"Enter weight of item {i+1}: "))
		items.append((v, w))
	max_value = fractional_knapsack(W, items)
	print(f"Maximum achievable value: {max_value}")
