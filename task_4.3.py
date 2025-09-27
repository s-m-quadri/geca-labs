# #Task 4.3: Reverse a String
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
# -------------------------
# Reverse a String
# -------------------------

# Recursive approach
def reverse_recursive(s):
    if len(s) <= 1:  # base case
        return s
    return reverse_recursive(s[1:]) + s[0]

# Iterative approach
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # prepend each character
    return reversed_str

# -------------------------
# Example usage
# -------------------------
s = "hello"
print("Recursive:", reverse_recursive(s))  # Output: "olleh"
print("Iterative:", reverse_iterative(s))  # Output: "olleh"

