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
    result = ""
    for char in s:
        result = char + result
    return result

def reverse_iterative_v2(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)

test_string = "hello"
print(f"Original string: '{test_string}'")
print(f"Recursive reverse: '{reverse_recursive(test_string)}'")
print(f"Iterative reverse: '{reverse_iterative(test_string)}'")
print(f"Iterative reverse v2: '{reverse_iterative_v2(test_string)}'")

test_string2 = "Python Programming"
print(f"\nOriginal string: '{test_string2}'")
print(f"Recursive reverse: '{reverse_recursive(test_string2)}'")
print(f"Iterative reverse: '{reverse_iterative(test_string2)}'")
print(f"Iterative reverse v2: '{reverse_iterative_v2(test_string2)}'")
