# ✅ TASK:
# Ask user for a sentence.
# Then:
#  - Print it in uppercase.
#  - Print it reversed.
#  - Print its length.

# 💡 TIP:
# Use `.upper()`, slicing `[::-1]`, and `len()`.
#code
# Get user input
sentence = input("Please enter a sentence: ")
# Print the sentence in uppercase
print("Uppercase:", sentence.upper())
# Print the sentence reversed
print("Reversed:", sentence[::-1])
# Print the length of the sentence
print("Length:", len(sentence))
