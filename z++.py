# Ask for a full name and display:
#  - All lowercase
#  - All uppercase
#  - Only initials (e.g., A. B. C.)

# 💡 TIP:
# Use `.split()` and `.upper()` / `.lower()`
a = float(input("First number: "))
op = input("Operator (+ - * /): ")
b = float(input("Second number: "))
if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print(a / b)
else: print("Invalid operator")