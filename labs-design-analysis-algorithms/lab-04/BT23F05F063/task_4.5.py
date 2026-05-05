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
    denominations: list of coin values (e.g., [1, 2, 5, 10, 20, 50, 100])
    amount: total amount to make change for
    Returns: tuple (total_coins_used, list_of_coins)
    """
    # Sort coins in descending order
    denominations.sort(reverse=True)
    
    coins_used = []
    remaining_amount = amount

    for coin in denominations:
        while remaining_amount >= coin:
            remaining_amount -= coin
            coins_used.append(coin)
    
    total_coins = len(coins_used)
    return total_coins, coins_used

# Example usage
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
total_coins, coins_used = greedy_coin_change(denominations, amount)

print(f"Minimum coins used: {total_coins}")
print("Coins used:", coins_used)
