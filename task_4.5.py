def greedy_coin_change(denominations, amount):
    """
    denominations: list of coin values
    amount: total amount to make change for
    Returns: list of coins used
    """
    # Sort denominations in descending order
    denominations.sort(reverse=True)
    
    coins_used = []
    remaining = amount
    
    for coin in denominations:
        while remaining >= coin:
            remaining -= coin
            coins_used.append(coin)
    
    return coins_used

# Test the function
denominations = list(map(int, input("Enter denominations separated by space: ").split()))
amount = int(input("Enter the amount: "))

coins = greedy_coin_change(denominations, amount)
print(f"Coins used: {coins}")
print(f"Total coins: {len(coins)}")
