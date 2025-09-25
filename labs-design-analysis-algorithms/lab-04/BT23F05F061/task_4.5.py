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


def coin_change_greedy(denominations, amount):
    # Sort denominations in descending order
    denominations.sort(reverse=True)
    
    result = []
    total_coins = 0

    for coin in denominations:
        while amount >= coin:
            amount -= coin
            result.append(coin)
            total_coins += 1

    return total_coins, result


# Example usage
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
coins_used, chosen = coin_change_greedy(denominations, amount)

print(f"Minimum coins: {coins_used}")
print("Coins used:", chosen)
