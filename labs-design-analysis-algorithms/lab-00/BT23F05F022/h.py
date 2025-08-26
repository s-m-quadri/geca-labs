# Create a list of 5 integers.
# Print the first, middle, and last elements.
# Modify the third element to be 100, then print the entire list.

# 💡 TIP:
# Use indexing like list[0], list[-1], and list[2] to access or change values.

list=[4,9,8,1,2]
print(f"first:{list[1]} middle:{list[len(list)//2]} last:{list[-1]}")
list[2]=100
for i in list:
    print(i,end=" ")
else:
    print()