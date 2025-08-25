# -------------------------------------------
# Problem: Print each letter of a word
# Example: "cat" → c a t
# -------------------------------------------

def print_letters_recursive(word, i=0):
    if i >= len(word):
        return
    print(word[i])
    print_letters_recursive(word, i + 1)

def print_letters_iterative(word):
    for ch in word:
        print(ch)

if __name__ == "__main__":
    word = input("Enter a word: ")
    print("Recursive:")
    print_letters_recursive(word)
    print("\nIterative:")
    print_letters_iterative(word)
