# Create a dictionary with 3 student names and their marks.
# Print a specific student’s marks.
# Loop through all students and print their names and scores.

dict = {"Bharti":99,"Tanvi":98,"Rashi":97}

print("Marks of Bharti : ",dict["Bharti"])

for name in dict:
    print(name," : ",dict[name])
# 💡 TIP:
# Use dict[key] to access values, and `.items()` to loop.
