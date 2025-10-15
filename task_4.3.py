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
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

def reverse_iterative(s):
    """Reverse a string using iteration (without slicing [::-1])."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_iterative_list(s):
    """Alternative iterative approach using list for better performance."""
    char_list = list(s)
    left, right = 0, len(char_list) - 1

    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    return ''.join(char_list)

if __name__ == "__main__":
    # Test strings
    test_strings = ["hello", "world", "python", "a", "", "racecar"]

    print("Testing String Reversal Functions:")
    print("-" * 50)

    for s in test_strings:
        rec_result = reverse_recursive(s)
        iter_result = reverse_iterative(s)
        iter_list_result = reverse_iterative_list(s)

        print(f"Original: '{s}'")
        print(f"  Recursive: '{rec_result}'")
        print(f"  Iterative: '{iter_result}'")
        print(f"  Iter List: '{iter_list_result}'")
        print(f"  All match: {rec_result == iter_result == iter_list_result}")
        print()