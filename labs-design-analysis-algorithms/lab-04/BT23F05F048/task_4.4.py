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

def fractional_knapsack(c, it):
    it = sorted(it, key=lambda x: x[0]/x[1], reverse=True)
    tv = 0.0
    for v, w in it:
        if c <= 0:
            break
        if w <= c:
            tv += v
            c -= w
        else:
            tv += v * (c / w)
            c = 0
    return tv

if __name__ == "__main__":
    c = 50
    it = [(60, 10), (100, 20), (120, 30)]
    mv = fractional_knapsack(c, it)
    print(f"Maximum achievable value in the knapsack: {mv}")
