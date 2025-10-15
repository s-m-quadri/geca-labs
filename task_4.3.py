# Recursive version
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]


# Iterative version
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # prepend each character
    return reversed_str


# Example usage
s = "hello"
print("Recursive:", reverse_recursive(s))  # Output: "olleh"
print("Iterative:", reverse_iterative(s))  # Output: "olleh"
