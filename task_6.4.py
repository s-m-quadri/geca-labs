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
    # Recursively find the root parent of x
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]        
def union(parent, x, y):
    # Find root parents of x and y
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootY] = rootX  # Merge y's set into x's set
# Example usage
parent = [0, 1, 2, 3]
print("Initial parent array:", parent)
union(parent, 0, 1)
print("Parent array after union(0, 1):", parent)
print("Find(1):", find(parent, 1))  # Should return 0
union(parent, 1, 2)
print("Parent array after union(1, 2):", parent)
print("Find(2):", find(parent, 2))  # Should return 0
print("Find(3):", find(parent, 3))  # Should return 3 (no union yet)    
