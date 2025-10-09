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
   
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

def reverse_iterative(s):
   
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  
    return reversed_s

def reverse_iterative_no_slice(s):
   
    reversed_chars = []
    for char in s:
        reversed_chars.insert(0, char)  
    return ''.join(reversed_chars)

s = "hello"
print("Input:", s)
print("Reversed (Recursive):", reverse_recursive(s))
print("Reversed (Iterative):", reverse_iterative(s))
print("Reversed (Iterative, no slice):", reverse_iterative_no_slice(s))

