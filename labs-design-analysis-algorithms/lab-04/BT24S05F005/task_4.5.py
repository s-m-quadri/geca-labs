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

    denominations.sort(reverse=True)
    
    coins_used = []
    remaining = amount

    for coin in denominations:
        while remaining >= coin:
            coins_used.append(coin)
            remaining -= coin

    if remaining != 0:
        print("Warning: Cannot make exact change with given denominations.")

    return len(coins_used), coins_used


# Example
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93

count, used_coins = coin_change_greedy(denominations, amount)
print(f"Total coins used: {count}")             # Output: 5
print(f"Coins used: {used_coins}")              # Output: [50, 20, 20, 2, 1]
