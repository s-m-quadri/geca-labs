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

def greedy_coin_change(denominations, amount):
    """
    Compute minimum coins for given amount using greedy algorithm.
    Parameters:
        denominations (list): List of coin denominations
        amount (int): Amount to make change for
    Returns:
        tuple: (total_coins_used, list_of_coins)
    """
    denominations = sorted(denominations, reverse=True)

    coins_used = []
    for coin in denominations:
        while amount >= coin:
            amount -= coin
            coins_used.append(coin)

    total_coins = len(coins_used)
    return total_coins, coins_used


denominations1 = [1, 2, 5, 10, 20]
amount1 = 93
total_coins1, coins_used1 = greedy_coin_change(denominations1, amount1)
print("Example 1:")
print("Amount:", amount1)
print("Total coins used:", total_coins1)
print("Coins used:", coins_used1)


denominations2 = [1, 5, 10, 25]
amount2 = 87
total_coins2, coins_used2 = greedy_coin_change(denominations2, amount2)
print("\nExample 2:")
print("Amount:", amount2)
print("Total coins used:", total_coins2)
print("Coins used:", coins_used2)


denominations3 = [1, 3, 4]
amount3 = 6
total_coins3, coins_used3 = greedy_coin_change(denominations3, amount3)
print("\nExample 3 (Greedy may fail):")
print("Amount:", amount3)
print("Total coins used:", total_coins3)
print("Coins used:", coins_used3)