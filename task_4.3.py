def reverse_recursive(s):
    if len(s) == 0: 
        return s
    return reverse_recursive(s[1:]) + s[0]

def reverse_iterative(s):
    reversed_str = ""
    for ch in s:             
        reversed_str = ch + reversed_str   
    return reversed_str

s = "hello"
print("Recursive reverse of", s, ":", reverse_recursive(s))
print("Iterative reverse of", s, ":", reverse_iterative(s))
