def fractional_knapsack(items, W):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0.0
    for value, weight in items:
        if W >= weight:
            total_value += value
            W -= weight
        else:
            total_value += value * (W / weight)
            break
    return total_value

capacity = 50
items = [(60,10), (100,20), (120,30)]
print(fractional_knapsack(items, capacity))

