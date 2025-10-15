# Task 4.1: Factorial (Recursive vs Iterative)
# -----------------------------------------
# Write two functions:
# 1. factorial_recursive(n): Uses recursion to compute factorial of n.
# 2. factorial_iterative(n): Uses loops to compute factorial of n.
#
# Input: an integer n (n >= 0)
# Output: factorial of n (n!)
#
# Example:
# Input: 5
# Output: 120
#
# Hint: Start with the mathematical definition:
# factorial(n) = 1 if n == 0 else n * factorial(n-1)
# Fractional Knapsack using Greedy Algorithm
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight
 
def fractional_knapsack(W, items):
    # Sort by value/weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
 
    total_value = 0.0
    for item in items:
        if W >= item.weight:
            W -= item.weight
            total_value += item.value
        else:
            total_value += item.value * (W / item.weight)
            break
    return total_value
 
# Driver
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
print("Maximum value in Knapsack =", fractional_knapsack(capacity, items))
