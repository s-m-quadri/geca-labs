def coin_change_greedy(denominations, amount):
    denominations.sort(reverse=True)
    coins_used = []
    for coin in denominations:
        while amount >= coin:
            amount -= coin
            coins_used.append(coin)
    return coins_used, len(coins_used)

denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
coins, count = coin_change_greedy(denominations, amount)
print(count, coins)
