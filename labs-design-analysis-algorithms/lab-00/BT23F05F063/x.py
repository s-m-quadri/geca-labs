# Create a simple game that:
#  - Rolls two dice
#  - Adds their values
#  - Tells if the player wins (sum > 7) or loses (sum <= 7)

# 💡 TIP:
# Use random.randint() twice and add the results

import random

def roll_dice():
    return random.randint(1, 6)

# Roll two dice
dice1 = roll_dice()
dice2 = roll_dice()
total = dice1 + dice2

print(f"You rolled: {dice1} and {dice2}")
print(f"Total: {total}")

if total > 7:
    print("You win!")
else:
    print("You lose!")
