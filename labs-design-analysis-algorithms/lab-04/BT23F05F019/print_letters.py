# -------------------------------------------
# Problem: Print each letter of a word
# Example: "cat" → c a t
# -------------------------------------------

# Recursive version
def print_letters_recursive(word, i=0):
    if i >= len(word):
        return
    print(word[i])
    print_letters_recursive(word, i + 1)

# Iterative version
def print_letters_iterative(word):
    for ch in word:
        print(ch)

# Try both
print_letters_recursive("dog")
print_letters_iterative("dog")
