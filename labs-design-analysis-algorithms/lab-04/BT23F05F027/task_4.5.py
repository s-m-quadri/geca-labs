# Task 4.5: Coin Change (Greedy)
# ----------------------------
# You have coins of certain denominations. 
# Write a greedy algorithm to make change for an amount using the fewest coins.
#
# Input:
# - List of denominations (e.g., [1, 2, 5, 10, 20, 50, 100])
# - Amount (e.g., 93)
#
# Output:
# - Minimum number of coins and which coins are used.
#
# Example:
# Denominations = [1, 2, 5, 10, 20, 50, 100]
# Amount = 93
# Output: 5 coins (50 + 20 + 20 + 2 + 1)
#
# Note: Greedy works with canonical coin systems like Indian/US coins,
# but may fail with arbitrary denominations. That’s the fun part to test!
# task_4.5.py
# Example: Find the index of an element in a list

def find_index(arr, target):
	for i, num in enumerate(arr):
		if num == target:
			return i
	return -1

if __name__ == "__main__":
	arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
	target = 9
	print(f"Index of {target}:", find_index(arr, target))
