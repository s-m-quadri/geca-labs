# ✅ TASK:
# Ask user for a sentence.
# Then:
#  - Print it in uppercase.
#  - Print it reversed.
#  - Print its length.

# 💡 TIP:
# Use `.upper()`, slicing `[::-1]`, and `len()`.

sentence = input("Enter a sentence: ")

print(f"Uppercase: {sentence.upper()}")

print(f"Reversed: {sentence[::-1]}")

print(f"Length: {len(sentence)}")