# Print the numbers from 1 to 10 using:
#  - a for loop
#  - a while loop

# 💡 TIP:
# `range(1, 11)` gives 1 through 10.
# Use `while` with a counter.

#solution
# For loop
for i in range(1, 11):
    print(i, end=' ')
print()

# While loop
count = 1
while count <= 10:
    print(count, end=' ')
    count += 1
print()