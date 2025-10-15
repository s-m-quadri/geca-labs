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
# task_4.4.py
# Example: Calculate the average of elements in a list

def average(arr):
	if not arr:
		return None
	return sum(arr) / len(arr)

if __name__ == "__main__":
	arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
	print("Average:", average(arr))
