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

from typing import List


def coin_change_greedy(denominations: List[int], amount: int) -> List[int]:
    """
    Greedy coin change. Returns list of coins used (largest-first).
    Raises ValueError if exact change cannot be made.
    """
    if not all(isinstance(d, int) and d > 0 for d in denominations):
        raise TypeError("denominations must be positive integers")
    if not isinstance(amount, int) or amount < 0:
        raise ValueError("amount must be a non-negative integer")

    denoms = sorted(set(denominations), reverse=True)
    remaining = amount
    result = []
    for d in denoms:
        if remaining <= 0:
            break
        count = remaining // d
        if count:
            result.extend([d] * count)
            remaining -= d * count

    if remaining != 0:
        raise ValueError(f"cannot make exact change for amount {amount} with given denominations")
    return result


if __name__ == "__main__":
    denoms = [1, 2, 5, 10, 20, 50, 100]
    amount = 93
    coins = coin_change_greedy(denoms, amount)
    print(f"{amount} => {len(coins)} coins: {coins}")
