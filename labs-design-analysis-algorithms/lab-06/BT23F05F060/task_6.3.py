
# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.
#
def create_parent_array(n):
	"""
	Creates a parent array for union-find with n vertices.
	Initially, parent[i] = i for all i.
	"""
	parent = [i for i in range(n)]
	print("Initial parent array:", parent)
	return parent


if __name__ == "__main__":
	n = 5
	create_parent_array(n)
