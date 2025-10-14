# ✅ TASK:
# Ask user for a sentence.
# Then:
#  - Print it in uppercase.
#  - Print it reversed.
#  - Print its length.

# 💡 TIP:
# Use `.upper()`, slicing `[::-1]`, and `len()`.
# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Print in uppercase
print("Uppercase:", sentence.upper())

# Print reversed
print("Reversed:", sentence[::-1])

# Print length
print("Length:", len(sentence))
