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


# Task 4.5: Coin Change (Greedy)
# ------------------------------

# Task 4.5: Coin Change (Greedy)
# ------------------------------

def greedy_coin_change(denominations, amount):
    
    denominations.sort(reverse=True)

    coins_used = []
    total_coins = 0
    remaining = amount

    for coin in denominations:
        while remaining >= coin:
            remaining -= coin
            coins_used.append(coin)
            total_coins += 1

        if remaining == 0:
            break


    if remaining != 0:
        return "Change cannot be made exactly with the given denominations."

    return total_coins, coins_used


if __name__ == "__main__":
    denominations = [1, 2, 5, 10, 20, 50, 100]
    amount = 93

    result = greedy_coin_change(denominations, amount)
    if isinstance(result, tuple):
        total_coins, coins = result
        print(f"Minimum coins needed: {total_coins}")
        print("Coins used:", coins)
    else:
        print(result)
