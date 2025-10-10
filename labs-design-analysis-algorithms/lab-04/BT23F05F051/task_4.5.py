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
# ---------------- Greedy Coin Change ----------------

def greedy_coin_change(denominations, amount):
    """
    denominations: list of coin values
    amount: total amount to make change for
    Returns: (total number of coins, list of coins used)
    """
    # Sort denominations in descending order
    denominations = sorted(denominations, reverse=True)
    
    coins_used = []
    remaining_amount = amount

    for coin in denominations:
        while remaining_amount >= coin:
            remaining_amount -= coin
            coins_used.append(coin)

        if remaining_amount == 0:
            break

    if remaining_amount != 0:
        print("Cannot make exact change with given denominations!")
    
    return len(coins_used), coins_used


# -------------------- Main Program --------------------
if __name__ == "__main__":
    # Input denominations
    denominations_input = input("Enter coin denominations separated by space (e.g., 1 2 5 10 20 50 100): ")
    denominations = list(map(int, denominations_input.split()))

    # Input amount
    amount = int(input("Enter the amount to make change for: "))

    num_coins, coins_used = greedy_coin_change(denominations, amount)

    print(f"\nMinimum number of coins needed: {num_coins}")
    print(f"Coins used: {coins_used}")
