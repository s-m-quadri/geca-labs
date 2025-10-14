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
# Recursive approach
def reverse_recursive(s):
    if len(s) == 0:  # Base case: empty string
        return ""
    else:
        return s[-1] + reverse_recursive(s[:-1])  # Last char + reverse rest

# Iterative approach
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str

# Example usage
s = "hello"
print("Recursive reverse of", s, "is:", reverse_recursive(s))
print("Iterative reverse of", s, "is:", reverse_iterative(s))
