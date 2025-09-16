# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.
import random

# Simulate a dice roll (1 to 6)
dice_roll = random.randint(1, 6)
print("Dice roll:", dice_roll)

# Simulate a coin toss
coin_toss = random.choice(["Heads", "Tails"])
print("Coin toss:", coin_toss)
