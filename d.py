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
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
def sum(num1,num2):
    return num1+num2
def diff(num1,num2):
    return num1-num2
def prod(num1,num2):
    return num1*num2
def quotient(num1,num2):
    return num1/num2
def power(num1,num2):
    return num1**num2

print("Sum:",sum(num1,num2))
print("Difference:",diff(num1,num2))
print("Prod:",prod(num1,num2))
print("Quotient:",quotient(num1,num2))
print("Power:",power(num1,num2))