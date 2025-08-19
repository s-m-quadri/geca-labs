# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.
import random

dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

coin_toss = random.choice(["Heads", "Tails"])
print(f"Coin toss: {coin_toss}")

print("\nMultiple simulations:")
for i in range(5):
    dice = random.randint(1, 6)
    coin = random.choice(["Heads", "Tails"])
    print(f"Round {i+1}: Dice = {dice}, Coin = {coin}")