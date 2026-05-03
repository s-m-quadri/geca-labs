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

parent = [0, 1, 2, 3]

def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:
        parent[root_y] = root_x

print("Initial parent:", parent)

union(0, 1)
print("Parent after union(0,1):", parent)
print("Find(1):", find(1))

union(1, 2)
print("Parent after union(1,2):", parent)
print("Find(2):", find(2))

union(3, 2)
print("Parent after union(3,2):", parent)
print("Find(3):", find(3))
