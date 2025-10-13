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

def coin_change(d, a):
    d.sort(reverse=True)
    r = []
    for c in d:
        while a >= c:
            a -= c
            r.append(c)
    if a > 0:
        return None
    return r

if __name__ == "__main__":
    d = [1, 2, 5, 10, 20, 50, 100]
    a = 93
    res = coin_change(d, a)
    if res is not None:
        print(f"Minimum number of coins: {len(res)}")
        print(f"Coins used: {res}")
    else:
        print("Change cannot be made with the given denominations.")
