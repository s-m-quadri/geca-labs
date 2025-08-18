# Import the `math` module and use it to calculate:
#  - The square root of 144
#  - The value of π
#  - sin(90 degrees) converted to radians

# 💡 TIP:
# Use `import math`, and remember degrees must be converted to radians.

import math

sqrt_144 = math.sqrt(144)
print(f"Square root of 144: {sqrt_144}")

pi_value = math.pi
print(f"Value of π: {pi_value}")

degrees = 90
radians = math.radians(degrees)
sin_90 = math.sin(radians)
print(f"sin(90 degrees): {sin_90}")