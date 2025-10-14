
my_tuple = (1, 2, 3)
try:
	my_tuple[1] = 99
except TypeError as e:
	print("Error:", e)
for item in my_tuple:
	print(item)
