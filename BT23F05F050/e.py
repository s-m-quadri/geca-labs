# ✅ TASK:
# Ask user for a sentence.
# Then:
#  - Print it in uppercase.
#  - Print it reversed.
#  - Print its length.

# 💡 TIP:
# Use `.upper()`, slicing `[::-1]`, and `len()`.


x = input("Enter a sentence: ")
print("Uppercase:", x.upper())
print("Reversed:", x[::-1])
print("Length:", len(x))
