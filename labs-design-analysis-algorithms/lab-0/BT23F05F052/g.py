# Print the numbers from 1 to 10 using:
#  - a for loop
#  - a while loop

# 💡 TIP:
# `range(1, 11)` gives 1 through 10.
# Use `while` with a counter.

print("Using for loop:")
for i in range(1, 11):
    print(i, end=' ')
print()

print("Using while loop:")
counter = 1
while counter <= 10:
    print(counter, end=' ')
    counter += 1
print()