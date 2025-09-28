def fractional_knapsack(capacity, items):
    items = sorted(items, key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0.0  
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break   

    return total_value

capacity = 50
items = [(60, 10), (100, 20), (120, 30)]  
print("Maximum achievable value:", fractional_knapsack(capacity, items))
