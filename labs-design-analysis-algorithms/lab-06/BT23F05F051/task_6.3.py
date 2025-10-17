# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.

def initialize_parent(n):
	"""
	Initializes parent array for union-find such that parent[i] = i.
	Returns the parent array and prints it.
	"""
	parent = [i for i in range(n)]
	print("Initial parent array:", parent)
	return parent

# Example usage
if __name__ == "__main__":
	num_vertices = 5
	initialize_parent(num_vertices)
