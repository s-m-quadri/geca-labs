# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.

import random

# Simulate dice roll
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

# Simulate coin toss
coin_options = ["Heads", "Tails"]
coin_toss = random.choice(coin_options)
print(f"Coin toss: {coin_toss}")
