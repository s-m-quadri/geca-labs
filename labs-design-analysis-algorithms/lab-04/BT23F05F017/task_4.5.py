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
    """
    Greedy algorithm for coin change problem.
    
    Args:
        denominations: List of coin denominations (sorted in descending order)
        amount: Target amount to make change for
    
    Returns:
        tuple: (total_coins, coins_used, success)
        coins_used is list of coins used
        success indicates if exact change was possible
    """
    if amount < 0:
        return 0, [], False

    if amount == 0:
        return 0, [], True

    # Sort denominations in descending order
    denominations = sorted(denominations, reverse=True)

    coins_used = []
    remaining_amount = amount

    for coin in denominations:
        if coin <= remaining_amount:
            # Calculate how many of this coin we can use
            count = remaining_amount // coin

            # Add coins to the result
            for _ in range(count):
                coins_used.append(coin)

            # Update remaining amount
            remaining_amount -= count * coin

            # If we've made exact change, stop
            if remaining_amount == 0:
                break

    success = remaining_amount == 0
    return len(coins_used), coins_used, success

def print_coin_change_solution(denominations, amount, total_coins, coins_used, success):
    """Print detailed solution of coin change problem."""
    print(f"Denominations: {denominations}")
    print(f"Amount: {amount}")

    if success:
        print(f"Total coins needed: {total_coins}")
        print(f"Coins used: {coins_used}")

        # Group coins by denomination for better display
        coin_count = {}
        for coin in coins_used:
            coin_count[coin] = coin_count.get(coin, 0) + 1

        print("Breakdown:")
        for coin in sorted(coin_count.keys(), reverse=True):
            count = coin_count[coin]
            print(f"  {count} × {coin} = {count * coin}")

        # Verify the solution
        total_value = sum(coins_used)
        print(f"Total value: {total_value} (should equal {amount})")
    else:
        print("Cannot make exact change with given denominations!")

if __name__ == "__main__":
    # Test case from the example
    denominations1 = [1, 2, 5, 10, 20, 50, 100]
    amount1 = 93

    print("Test Case 1 (Standard denominations):")
    print("=" * 50)
    total_coins1, coins_used1, success1 = coin_change_greedy(denominations1, amount1)
    print_coin_change_solution(denominations1, amount1, total_coins1, coins_used1, success1)
    print()

    # Test case with different amount
    amount2 = 67
    print("Test Case 2 (Different amount):")
    print("=" * 50)
    total_coins2, coins_used2, success2 = coin_change_greedy(denominations1, amount2)
    print_coin_change_solution(denominations1, amount2, total_coins2, coins_used2, success2)
    print()

    # Test case where greedy might not work optimally
    denominations3 = [1, 3, 4]
    amount3 = 6
    print("Test Case 3 (Non-canonical system - greedy may be suboptimal):")
    print("=" * 50)
    total_coins3, coins_used3, success3 = coin_change_greedy(denominations3, amount3)
    print_coin_change_solution(denominations3, amount3, total_coins3, coins_used3, success3)
    print("Note: Optimal solution would be 2 coins (3+3), but greedy gives 3 coins (4+1+1)")
