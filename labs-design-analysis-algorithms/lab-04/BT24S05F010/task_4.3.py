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

def reverse_recursive(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_recursive(s[:-1])

def reverse_iterative(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

s = "hello"
print("Original string:", s)
print("Reversed string (recursive):", reverse_recursive(s))
print("Reversed string (iterative):", reverse_iterative(s))
