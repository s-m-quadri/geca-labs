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


# Function 1: Recursive approach
def reverse_recursive(s):
    if len(s) <= 1:   # Base case
        return s
    return reverse_recursive(s[1:]) + s[0]


# Function 2: Iterative approach
def reverse_iterative(s):
    result = ""
    for char in s:
        result = char + result   # Prepend each character
    return result


# Example usage
s = "hello"
print("Recursive:", reverse_recursive(s))  # Output: "olleh"
print("Iterative:", reverse_iterative(s))  # Output: "olleh"
