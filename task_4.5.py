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
    # Step 1: Sort denominations in descending order
    denominations.sort(reverse=True)
    
    coins_used = []
    remaining_amount = amount
    
    # Step 2: Pick the largest coin possible at each step
    for coin in denominations:
        while remaining_amount >= coin:
            remaining_amount -= coin
            coins_used.append(coin)
    
    if remaining_amount != 0:
        print("Greedy approach cannot make exact change with given denominations.")
    
    return coins_used, len(coins_used)

# Example usage
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
coins, count = coin_change_greedy(denominations, amount)

print(f"Minimum number of coins: {count}")
print(f"Coins used: {coins}")
