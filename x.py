# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.

import random

# Simulate a dice roll (1 to 6)
dice_roll = random.randint(1, 6)

# Simulate a coin toss (Heads or Tails)
coin_toss = random.choice(["Heads", "Tails"])

# Print the results
print("Dice roll:", dice_roll)
print("Coin toss:", coin_toss)
