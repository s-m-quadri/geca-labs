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

# ---------------- String Reversal Functions ----------------

# Recursive string reversal
def reverse_recursive(s):
    if len(s) == 0 or len(s) == 1:
        return s
    else:
        # Reverse all except first character and append first character at the end
        return reverse_recursive(s[1:]) + s[0]

# Iterative string reversal
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str

# -------------------- Main Program --------------------
if __name__ == "__main__":
    s = input("Enter a string to reverse: ")

    rev_rec = reverse_recursive(s)
    rev_iter = reverse_iterative(s)

    print(f"Reversed string (recursive): {rev_rec}")
    print(f"Reversed string (iterative): {rev_iter}")
