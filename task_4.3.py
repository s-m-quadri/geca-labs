def reverse_recursive(s):
    if s == "":
        return ""
    return reverse_recursive(s[1:]) + s[0]

def reverse_iterative(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

s = "hello"
print(reverse_recursive(s))
print(reverse_iterative(s))
