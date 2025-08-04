# Write a program that takes two numbers from the user.
# Print their:
#  - sum
#  - difference
#  - product
#  - quotient
#  - remainder
#  - power (x^y)

# 💡 TIP:
# Use `+`, `-`, `*`, `/`, `%`, and `**`.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

sum = x + y
difference = x - y
product = x * y
quotient = x // y 
remainder = x % y
power = x ** y

print("sum : ",sum)
print("difference :",difference)
print("product : ",product)
print("quotient : ",quotient)
print("remainder : ",remainder)
print("power : ",power)

