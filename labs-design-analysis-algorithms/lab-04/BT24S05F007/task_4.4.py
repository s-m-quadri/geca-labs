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

from typing import List, Tuple


def fractional_knapsack(capacity: float, items: List[Tuple[float, float]]):
    """
    Solve fractional knapsack.
    items: list of (value, weight)
    Returns (max_value, taken) where taken is list of (value_taken, weight_taken, original_index)
    """
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    indexed = [(i, v, w) for i, (v, w) in enumerate(items)]
    # sort by value/weight descending
    indexed.sort(key=lambda x: (x[1] / x[2]) if x[2] > 0 else float("inf"), reverse=True)

    remaining = float(capacity)
    total_value = 0.0
    taken = []
    for idx, value, weight in indexed:
        if remaining <= 0:
            break
        if weight <= 0:
            continue
        if weight <= remaining:
            taken.append((value, weight, idx))
            total_value += value
            remaining -= weight
        else:
            fraction = remaining / weight
            total_value += value * fraction
            taken.append((value * fraction, remaining, idx))
            remaining = 0.0
            break
    return total_value, taken


if __name__ == "__main__":
    W = 50
    items = [(60, 10), (100, 20), (120, 30)]
    val, taken = fractional_knapsack(W, items)
    print("Max value:", val)
    print("Taken:", taken)
