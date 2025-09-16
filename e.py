# ✅ TASK:
# Ask user for a sentence.
# Then:
#  - Print it in uppercase.
#  - Print it reversed.
#  - Print its length.

# 💡 TIP:
# Use `.upper()`, slicing `[::-1]`, and `len()`.
# Asking user for a sentence
sentence = input("Enter a sentence: ")

# Printing results
print("Uppercase:", sentence.upper())
print("Reversed:", sentence[::-1])
print("Length:", len(sentence))
