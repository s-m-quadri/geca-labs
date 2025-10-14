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
    Greedy algorithm to make change using the fewest coins.

    Parameters:
    denominations : list[int] : coin denominations
    amount        : int       : total amount to change

    Returns:
    total_coins   : int       : minimum number of coins
    coins_used    : list[int] : list of coins used
    """
    # Sort denominations in descending order
    denominations.sort(reverse=True)

    coins_used = []
    remaining = amount

    for coin in denominations:
        while remaining >= coin:
            remaining -= coin
            coins_used.append(coin)

    if remaining != 0:
        print("Warning: Exact change not possible with given denominations.")
    
    return len(coins_used), coins_used


# --------------------------
# Example Usage
# --------------------------
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93

total_coins, coins_used = greedy_coin_change(denominations, amount)

print("Minimum number of coins:", total_coins)         # Output: 5
print("Coins used:", coins_used)                       # Output: [50, 20, 20, 2, 1]
