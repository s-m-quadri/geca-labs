Completed d.py
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

print("Enter a no : ")
a= int(input())
print("Enter a no : ")
b= int(input())
sum = a +b 
difference = a -b
product = a * b
quotient = a /b
remainder = a %b
power = a **b 

print(f"""
sum ={sum}
difference ={difference}
product ={product}
Quotient ={quotient}
Remainder ={remainder} 
Power = {power} """)



x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)
print("Remainder:", x % y)
print("Power:", x ** y)

