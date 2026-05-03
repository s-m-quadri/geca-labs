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


def reverse_recursive(s: str) -> str:
    """Reverse a string using recursion."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    if len(s) <= 1:
        return s
    return s[-1] + reverse_recursive(s[:-1])


def reverse_iterative(s: str) -> str:
    """Reverse a string using an iterative loop (no slicing shortcut)."""
    if not isinstance(s, str):
        raise TypeError("s must be a string")
    chars = []
    for ch in s:
        chars.insert(0, ch)
    return "".join(chars)


if __name__ == "__main__":
    test = "hello"
    print(test, "=>", reverse_recursive(test))
    print(test, "=>", reverse_iterative(test))
