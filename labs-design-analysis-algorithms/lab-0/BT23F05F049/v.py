# Import the `math` module and use it to calculate:
#  - The square root of 144
#  - The value of π
#  - sin(90 degrees) converted to radians

# 💡 TIP:
# Use `import math`, and remember degrees must be converted to radians.
import math
sqrt_144 = math.sqrt(144)
print("Square root of 144:", sqrt_144)

# Value of π
pi_value = math.pi
print("Value of π:", pi_value)

# sin(90 degrees) -> convert degrees to radians first
sin_90 = math.sin(math.radians(90))
print("sin(90°):", sin_90)