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

def coin_change_greedy(denominations, amount):
    """
    denominations: list of coin values
    amount: target amount to make
    """
    # Step 1: Sort denominations in descending order
    denominations.sort(reverse=True)

    coins_used = []  # to store selected coins
    remaining = amount

    # Step 2: Pick the largest coin possible each time
    for coin in denominations:
        while remaining >= coin:
            remaining -= coin
            coins_used.append(coin)

    # Step 3: Output total coins and which coins used
    print("Coins used:", coins_used)
    print("Total coins used:", len(coins_used))
    return coins_used

# Example usage
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93

print("Amount:", amount)
coin_change_greedy(denominations, amount)
