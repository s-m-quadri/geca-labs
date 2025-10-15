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
    """Reverse a string using recursion."""
    if len(s) == 0:
        return s
    return reverse_recursive(s[1:]) + s[0]

def reverse_iterative(s):
    """Reverse a string using a loop."""
    result = ""
    for char in s:
        result = char + result
    return result

# Example usage:
if __name__ == "__main__":
    s = "hello"
    print(f"Recursive: '{s}' -> '{reverse_recursive(s)}'")
    print(f"Iterative: '{s}' -> '{reverse_iterative(s)}'")
