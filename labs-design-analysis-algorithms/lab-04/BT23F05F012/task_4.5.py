# #Task 4.5: Coin Change (Greedy)
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
def coin_change_greedy(denominations, amount):
    """
    denominations: list of coin values
    amount: total amount to make
    Returns tuple: (total_coins, list_of_coins_used)
    """
    denominations.sort(reverse=True)  # start from largest coin
    coins_used = []
    total_coins = 0

    for coin in denominations:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            coins_used.extend([coin] * count)
            total_coins += count
            amount -= coin * count

    if amount != 0:
        return None  # Cannot make exact change with given coins
    return total_coins, coins_used


# -------------------------
# Example usage
# -------------------------
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
result = coin_change_greedy(denominations, amount)

if result:
    total_coins, coins_used = result
    print(f"Minimum coins: {total_coins}")
    print(f"Coins used: {coins_used}")
else:
    print("Change cannot be made with given denominations.")

