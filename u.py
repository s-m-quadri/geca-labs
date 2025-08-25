# Create a list of squares for numbers 1 to 10 using list comprehension.
#  - Also create a list of even numbers from 1 to 20.

# 💡 TIP:
# Format → `[expression for item in iterable if condition]`

sqr=[i*i for i in range(1,11)]
even=[i for i in range(1,21) if i%2==0 ]
print(sqr)
print(even)