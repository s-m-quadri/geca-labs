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
# coin_change_greedy.py
# Task 4.5: Coin Change (Greedy Algorithm)

def coin_change_greedy(denominations, amount):
    """
    Find minimum number of coins to make change for given amount using greedy approach.
    
    Parameters:
    - denominations: list of coin denominations
    - amount: int, target amount
    
    Returns:
    - Tuple: (total coins used, list of coins used)
    """
    # Sort denominations in descending order for greedy choice
    denominations.sort(reverse=True)
    
    coins_used = []
    remaining = amount
    
    for coin in denominations:
        while remaining >= coin:
            remaining -= coin
            coins_used.append(coin)
    
    total_coins = len(coins_used)
    
    return total_coins, coins_used


# Example usage
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
total, coins = coin_change_greedy(denominations, amount)
print(f"Amount: {amount}")
print(f"Minimum coins used: {total}")
print(f"Coins used: {coins}")
