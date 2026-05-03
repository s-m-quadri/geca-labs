# Fractional Knapsack using Greedy Algorithm
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight
 
def fractional_knapsack(W, items):
    # Sort by value/weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
 
    total_value = 0.0
    for item in items:
        if W >= item.weight:
            W -= item.weight
            total_value += item.value
        else:
            total_value += item.value * (W / item.weight)
            break
    return total_value
 
# Driver
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
print("Maximum value in Knapsack =", fractional_knapsack(capacity, items))