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
    return [i for i in range(n)]

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, x, y):
    rx = find(p, x)
    ry = find(p, y)
    if rx != ry:
        p[ry] = rx
    return p

n = 5
p = create_parent_array(n)
print("Initial parent array:", p)
p = union(p, 0, 1)
print("Parent array after union(0,1):", p)
p = union(p, 1, 2)
print("Parent array after union(1,2):", p)
print("Find(2):", find(p, 2))  # Should return 0
print("Find(3):", find(p, 3))  # Should return 3