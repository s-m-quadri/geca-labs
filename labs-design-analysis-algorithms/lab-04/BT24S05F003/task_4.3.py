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
# reverse_string_task.py
# Task 4.3: Reverse a String

def reverse_recursive(s):
    """Reverse a string using recursion"""
    if len(s) == 0:
        return ""
    # Take last character and reverse the rest
    return s[-1] + reverse_recursive(s[:-1])


def reverse_iterative(s):
    """Reverse a string using iteration"""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # prepend each character
    return reversed_str


# Example usage
s = "hello"
print(f"Original string: {s}")
print(f"Reversed (recursive): {reverse_recursive(s)}")  # Output: olleh
print(f"Reversed (iterative): {reverse_iterative(s)}")  # Output: olleh

