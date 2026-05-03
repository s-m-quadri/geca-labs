
def print_letters_recursive(word, i=0):
    if i >= len(word):
        return
    print(word[i])
    print_letters_recursive(word, i + 1)


def print_letters_iterative(word):
    for ch in word:
        print(ch)

word = "dog"
print("Recursive:")
print_letters_recursive(word)

print("\nIterative:")
print_letters_iterative(word)
