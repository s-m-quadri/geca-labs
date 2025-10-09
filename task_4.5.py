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
# ----------------------------
# Task 4.5: Coin Change (Greedy)
# ----------------------------

def coin_change_greedy(coins, amount):
    """Greedy algorithm to make change using the fewest coins."""
    
    # Step 1: Sort coins in descending order
    coins.sort(reverse=True)
    
    result = []  # To store coins used
    remaining = amount
    
    # Step 2: Pick the largest possible coin each time
    for coin in coins:
        if coin <= remaining:
            count = remaining // coin  # Number of coins of this denomination
            remaining -= count * coin
            result.append((coin, count))
    
    # Step 3: Check if exact change was possible
    if remaining != 0:
        print("Exact change cannot be made with given denominations.")
    else:
        print(f"Change for {amount}:")
        for coin, count in result:
            print(f"{coin} x {count}")
    
    return result


# Example usage:
coins = [10, 5, 2, 1]   # Coin denominations
amount = 27              # Amount to make change for

coin_change_greedy(coins, amount)
