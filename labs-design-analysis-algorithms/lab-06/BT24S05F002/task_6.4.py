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
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    """
    Merges the sets containing x and y.
    """
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[yroot] = xroot

if __name__ == "__main__":
    parent = [0, 1, 2, 3]
    union(parent, 0, 1)
    print("Parent after union(0,1):", parent)
    print("find(1):", find(parent, 1))
    union(parent, 1, 2)
    print("Parent after union(1,2):", parent)
    print("find(2):", find(parent, 2))
