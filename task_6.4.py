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
# Task 6.4: Find and Union Functions
# -----------------------------------

def find(parent, x):
    """
    Recursively finds the root parent of x.
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])  # Recursive call


def union(parent, x, y):
    """
    Merges the sets containing x and y.
    Sets the parent of y's root to x's root.
    """
    root
