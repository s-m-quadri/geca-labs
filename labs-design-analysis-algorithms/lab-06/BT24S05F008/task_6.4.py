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
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[yroot] = xroot

parent = [0, 1, 2, 3]
union(parent, 0, 1)
union(parent, 1, 2)

print("Parent array:", parent)
print("Find 2:", find(parent, 2))
print("Find 3:", find(parent, 3))
