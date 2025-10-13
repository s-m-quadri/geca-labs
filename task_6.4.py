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


def create_parent_array(n):
    # Initialize parent array
    return [i for i in range(n)]

def find(parent, x):
    # Recursively find root parent of x
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    # Find roots of both elements
    root_x = find(parent, x)
    root_y = find(parent, y)

    # Merge sets if they have different roots
    if root_x != root_y:
        parent[root_y] = root_x  # attach y’s root under x’s root

# Example usage
n = 4
parent = create_parent_array(n)
print("Initial parent:", parent)

union(parent, 0, 1)
print("After union(0,1):", parent)

union(parent, 1, 2)
print("After union(1,2):", parent)

# Test find()
print("find(2):", find(parent, 2))
