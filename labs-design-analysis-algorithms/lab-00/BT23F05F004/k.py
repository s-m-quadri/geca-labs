
# 💡 TIP:
# Tuples are like lists, but immutable (they cannot be changed).

my_tuple = (1, 2, 3)
try:
    my_tuple[1] = 20 
except TypeError as e:
    print("Error:", e)
for item in my_tuple:
    print(item)
