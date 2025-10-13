# Import the `math` module and use it to calculate:
#  - The square root of 144
#  - The value of π
#  - sin(90 degrees) converted to radians

# 💡 TIP:
# Use `import math`, and remember degrees must be converted to radians.

import math

# Square root of 144
sqrt_val = math.sqrt(144)
print("Square root of 144:", sqrt_val)

# Value of π
pi_val = math.pi
print("Value of π:", pi_val)

# sin(90 degrees) → convert to radians first
radians_90 = math.radians(90)
sin_90 = math.sin(radians_90)
print("sin(90 degrees):", sin_90)
