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


def reverse_recursive(s):
    if len(s) == 0:
        return s
    return reverse_recursive(s[1:]) + s[0]


def reverse_iterative(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str  
    return reversed_str


if __name__ == "__main__":
    s = "hello"  

    print("Recursive reverse:", reverse_recursive(s))  
    print("Iterative reverse:", reverse_iterative(s))  