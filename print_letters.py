# -------------------------------------------
# Problem: Print each letter of a word
# Example: "cat" → c a t
# -------------------------------------------

# Recursive version (basic)
def fun(word, i=0):
    if i >= len(word):   # base case
        return
    print(word[i])
    fun(word, i+1)       # recursive call

# Recursive version (clear name)
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
word = "dog"
print("Recursive:")
print_letters_recursive(word)

word = "cat"
print("\nUsing fun():")
fun(word)

print("\nIterative:")
print_letters_iterative(word)
