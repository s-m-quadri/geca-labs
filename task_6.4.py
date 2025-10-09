
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

def find(x, parent):
	"""
	Recursively finds the root parent of x.
	"""
	if parent[x] != x:
		return find(parent[x], parent)
	return x

def union(x, y, parent):
	"""
	Merges sets containing x and y.
	"""
	x_root = find(x, parent)
	y_root = find(y, parent)
	if x_root != y_root:
		parent[y_root] = x_root

# Example usage
if __name__ == "__main__":
	parent = [0, 1, 2, 3]
	print("Initial parent:", parent)
	union(0, 1, parent)
	print("After union(0, 1):", parent)
	print("find(1):", find(1, parent))
	union(1, 2, parent)
	print("After union(1, 2):", parent)
	print("find(2):", find(2, parent))
