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
    Find the root parent of x using recursion.
    """
    if parent[x] == x:
        return x
    else:
        return find(parent, parent[x])

def union(parent, x, y):
    """
    Merge the sets containing x and y.
    """
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root  # Make x_root the parent of y_root

# Example usage
parent = [0, 1, 2, 3]
print("Initial parent:", parent)

union(parent, 0, 1)
print("Parent after union(0,1):", parent)
print("Find(1):", find(parent, 1))

union(parent, 1, 2)
print("Parent after union(1,2):", parent)
print("Find(2):", find(parent, 2))
