# Task 6.4: Find and Union Functions
# -----------------------------------
# Extend union-find with:
# 1. find(x) -> returns root parent of x.
# 2. union(x, y) -> merges sets containing x and y.

# Example:
# parent = [0,1,2,3]
# union(0,1) → parent updated
# find(1) → should return 0 after union

# Hint: Use recursion for find().
# Tip: Try multiple unions, like (0,1), (1,2).

def find(parent, x):
	"""
	Recursively finds the root parent of x.
	"""
	if parent[x] != x:
		parent[x] = find(parent, parent[x])  # Path compression
	return parent[x]

def union(parent, x, y):
	"""
	Merges sets containing x and y.
	"""
	root_x = find(parent, x)
	root_y = find(parent, y)
	if root_x != root_y:
		parent[root_y] = root_x

if __name__ == "__main__":
	parent = [0, 1, 2, 3]
	print("Initial parent:", parent)
	union(parent, 0, 1)
	print("After union(0,1):", parent)
	union(parent, 1, 2)
	print("After union(1,2):", parent)
	print("find(2):", find(parent, 2))
