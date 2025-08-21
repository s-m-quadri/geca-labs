# Write a program that prints each item of a list on a new line.
# Then, print the index and value using a loop.

# 💡 TIP:
# Use `for item in list` and `enumerate(list)` for both item and index.

cars = ["Tata", "Maruti", "Honda"]
for car in cars:
    print(car)

print("---")

for index, value in enumerate(cars):
    print(f"Index {index}: {value}")