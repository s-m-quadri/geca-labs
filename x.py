# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.
import random

# Simulate a dice roll (1 to 6)
def roll_dice():
    dice = random.randint(1, 6)
    print("Dice rolled:", dice)

# Simulate a coin toss (Heads or Tails)
def toss_coin():
    coin = random.choice(["Heads", "Tails"])
    print("Coin toss result:", coin)

# Example usage
roll_dice()
toss_coin()
