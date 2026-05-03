def coin_change_greedy(denominations, amount):
    """
    denominations: list of coin values
    amount: total amount to make change for
    returns: tuple (number of coins, list of coins used)
    """
    # Step 1: Sort denominations in descending order
    denominations.sort(reverse=True)
    
    coins_used = []
    remaining = amount

    for coin in denominations:
        while remaining >= coin:
            remaining -= coin
            coins_used.append(coin)
        if remaining == 0:
            break

    if remaining != 0:
        return "Change cannot be made exactly with given denominations"

    return len(coins_used), coins_used


# Example usage
denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
num_coins, coins_list = coin_change_greedy(denominations, amount)
print(f"Minimum coins needed: {num_coins}")
print(f"Coins used: {coins_list}")
# Output: Minimum coins needed: 5
# Coins used: [50, 20, 20, 2, 1]
