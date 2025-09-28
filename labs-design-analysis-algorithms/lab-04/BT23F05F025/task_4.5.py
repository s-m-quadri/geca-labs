def coin_change_greedy(denominations, amount):
    denominations.sort(reverse=True)
    result = []
    for coin in denominations:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result

denominations = [1, 2, 5, 10, 20, 50, 100]
amount = 93
coins_used = coin_change_greedy(denominations, amount)
print("Minimum coins:", len(coins_used))
print("Coins used:", coins_used)
