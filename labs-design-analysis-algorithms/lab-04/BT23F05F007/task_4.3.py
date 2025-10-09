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
# Task 4.3: Reverse a String
# --------------------------

# 1️⃣ Recursive method
def reverse_recursive(s):
    # Base case: if the string is empty or has one character, return it
    if len(s) <= 1:
        return s
    # Recursive step: reverse the substring and add the first character at the end
    return reverse_recursive(s[1:]) + s[0]


# 2️⃣ Iterative method
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # add each character in front
    return reversed_str


# Example usage
s = "hello"
print("Original string:", s)
print("Reversed (recursive):", reverse_recursive(s))
print("Reversed (iterative):", reverse_iterative(s))
