# Task 4.3: Reverse a String
# ------------------------
# Write two functions to reverse a string:
# 1. reverse_recursive(s): Reverse the string using recursion.
# 2. reverse_iterative(s): Reverse the string using a loop.
#
# Input: string s
# Output: reversed string
#
# Example:
# Input: "hello"
# Output: "olleh"
#
# Bonus: Try solving without using Python slicing [::-1].
# ------------------------
# Task 4.3: Reverse a String
# ------------------------

# 1️⃣ Recursive approach
def reverse_recursive(s):
    """Reverse a string using recursion."""
    if len(s) == 0:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]


# 2️⃣ Iterative approach
def reverse_iterative(s):
    """Reverse a string using a loop."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Add current char in front
    return reversed_str


# Example usage:
text = "Hello"
print(f"Original String: {text}")
print(f"Reversed (Recursive): {reverse_recursive(text)}")
print(f"Reversed (Iterative): {reverse_iterative(text)}")
