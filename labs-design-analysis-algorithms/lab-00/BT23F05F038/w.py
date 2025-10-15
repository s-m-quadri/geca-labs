# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.
import random

# Simulate a dice roll (1 to 6)
def roll_dice():
    return random.randint(1, 6)

# Simulate a coin toss (Heads or Tails)
def toss_coin():
    return random.choice(["Heads", "Tails"])

# Example usage
print("Dice rolled:", roll_dice())
print("Coin toss result:", toss_coin())
