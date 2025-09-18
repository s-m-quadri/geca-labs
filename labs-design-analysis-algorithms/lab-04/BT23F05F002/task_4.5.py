# Task 4.5: Coin Change (Greedy)
# ----------------------------
# You have coprint("Note: For this case, greedy gives 3 coins (4+1+1), but optimal is 2 coins (3+3)")minations. 
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
# but may fail with arbitrary denominations. That's the fun part to test!

def coin_change_greedy(denominations, amount):
    denominations.sort(reverse=True)
    
    result = []
    total_coins = 0
    remaining_amount = amount
    
    for coin in denominations:
        if remaining_amount >= coin:
            count = remaining_amount // coin
            result.extend([coin] * count)
            total_coins += count
            remaining_amount -= coin * count
    
    if remaining_amount > 0:
        return None, []
    
    return total_coins, result

def print_coin_change_solution(denominations, amount, num_coins, coins_used):
    print(f"Amount to change: {amount}")
    print(f"Available denominations: {denominations}")
    
    if num_coins is None:
        print("Cannot make exact change with given denominations!")
        return
    
    print(f"Minimum coins needed: {num_coins}")
    print(f"Coins used: {coins_used}")
    
    coin_count = {}
    for coin in coins_used:
        coin_count[coin] = coin_count.get(coin, 0) + 1
    
    print("Breakdown:")
    for coin in sorted(coin_count.keys(), reverse=True):
        count = coin_count[coin]
        print(f"  {count} x {coin} = {count * coin}")
    
    print(f"Total: {sum(coins_used)}")

denominations1 = [1, 2, 5, 10, 20, 50, 100]
amount1 = 93
num_coins1, coins_used1 = coin_change_greedy(denominations1, amount1)
print_coin_change_solution(denominations1, amount1, num_coins1, coins_used1)

print("\n" + "="*50)

denominations2 = [1, 5, 10, 25]
amount2 = 67
num_coins2, coins_used2 = coin_change_greedy(denominations2, amount2)
print_coin_change_solution(denominations2, amount2, num_coins2, coins_used2)

print("\n" + "="*50)

denominations3 = [4, 3, 1]
amount3 = 6
num_coins3, coins_used3 = coin_change_greedy(denominations3, amount3)
print_coin_change_solution(denominations3, amount3, num_coins3, coins_used3)
print("Note: For this case, greedy gives 3 coins (4+1+1), but optimal is 2 coins (3+3)")ange (Greedy)
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
