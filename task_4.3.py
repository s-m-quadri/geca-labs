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
# 1. Reverse a string using recursion
def reverse_recursive(s):
    if s == "":  # Base case: empty string
        return ""
    else:
        return reverse_recursive(s[1:]) + s[0]

# 2. Reverse a string using iteration
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str

# Test the functions
input_str = "hello"
print("Original:", input_str)
print("Reversed (recursive):", reverse_recursive(input_str))
print("Reversed (iterative):", reverse_iterative(input_str))
