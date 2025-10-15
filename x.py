# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.
# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.

import random

# Dice roll
dice = random.randint(1, 6)
print("Dice roll:", dice)

# Coin toss
coin = random.choice(["Heads", "Tails"])
print("Coin toss:", coin)