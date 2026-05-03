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

#solution
def reverse_recursive(s):
    """Reverse a string using recursion."""
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

def reverse_iterative(s):
    """Reverse a string using iteration (without slicing)."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


#Example (very important)
print("Recursive Reverse:")
print('Input: "Siddhesh" ->', reverse_recursive("Siddhesh")) 
print('Input: "Maria" ->', reverse_recursive("Maria"))  

print("\nIterative Reverse:")
print('Input: "Shivam" ->', reverse_iterative("Shivam"))  
print('Input: "Sarkaar" ->', reverse_iterative("Sarkaar"))  
