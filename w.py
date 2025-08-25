# Use `random` to simulate:
#  - A dice roll (1 to 6)
#  - A coin toss (Heads or Tails)

# 💡 TIP:
# Use `random.randint()` for numbers, and `random.choice()` for custom options.

import random
dice=random.randint(1,6)
coin=random.choice(["Heads","Tails"])
print(dice,coin)
