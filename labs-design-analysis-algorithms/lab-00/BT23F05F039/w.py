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

print("\nMultiple rolls:")
for i in range(3):
    print(f"Roll {i+1}: Dice = {random.randint(1, 6)}, Coin = {random.choice(['Heads', 'Tails'])}")