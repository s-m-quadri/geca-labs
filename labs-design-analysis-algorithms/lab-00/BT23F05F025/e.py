# ✅ TASK:
# Ask user for a sentence.
# Then:
#  - Print it in uppercase.
#  - Print it reversed.
#  - Print its length.

# 💡 TIP:
# Use `.upper()`, slicing `[::-1]`, and `len()`.

sentence = input("Write a sentence")
print("Uppercase:", sentence.upper())
print("Reversed:", sentence[::-1])
print("Length:", len(sentence))