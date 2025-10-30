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
    Find with recursion and path compression: returns root parent of x.
    parent: list where parent[i] is the parent of i
    """
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    """
    Merge sets containing x and y by linking roots.
    This version does not use rank; it sets root of y to root of x.
    Returns True if a merge happened, False if they were already connected.
    """
    rx = find(parent, x)
    ry = find(parent, y)
    if rx == ry:
        return False
    parent[ry] = rx
    return True

if __name__ == "__main__":
    p = [0,1,2,3]
    print("Initial parent:", p)
    union(p, 0, 1)
    print("After union(0,1):", p)
    print("find(1):", find(p, 1))
    union(p, 1, 2)
    print("After union(1,2):", p)
    print("find(2):", find(p, 2))
