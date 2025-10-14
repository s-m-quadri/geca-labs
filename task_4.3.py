# Recursive approach
def reverse_recursive(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_recursive(s[:-1])

# Iterative approach
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Test the functions
s = input("Enter a string: ")

print(f"Recursive reversal: {reverse_recursive(s)}")
print(f"Iterative reversal: {reverse_iterative(s)}")
