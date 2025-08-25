# Given a list of tuples containing student names and scores:
# students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
# Sort them in:
#     - Descending order of scores
#     - If scores are equal, ascending alphabetical order by name

# Expected Output:
# [("Bob", 92), ("David", 92), ("Alice", 85), ("Charlie", 78)]

# INSTRUCTIONS:
# - Implement merge sort to achieve the required sorting order.
# - Modify the comparison logic inside merge function accordingly.
# - Do not use Python's built-in sort().

# Write your solution here


def merge_sort_students(students):
	if len(students) <= 1:
		return students
	mid = len(students) // 2
	left = merge_sort_students(students[:mid])
	right = merge_sort_students(students[mid:])
	return merge(left, right)

def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
	
		if left[i][1] > right[j][1]:
			result.append(left[i])
			i += 1
		elif left[i][1] < right[j][1]:
			result.append(right[j])
			j += 1
		else:
			if left[i][0] < right[j][0]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
	result.extend(left[i:])
	result.extend(right[j:])
	return result

if __name__ == "__main__":
	students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 92)]
	print(merge_sort_students(students))