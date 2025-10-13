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

def create_parent_array(n):
    return [i for i in range(n)]


# Find function - returns the root parent of x
def find(parent, x):
    if parent[x] == x:
        return x
    # Recursively find the root parent
    return find(parent, parent[x])


# Union function - merges sets containing x and y
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x  # Attach one tree under another


# Example usage:
parent = create_parent_array(4)
print("Initial parent array:", parent)

union(parent, 0, 1)
print("After union(0,1):", parent)

union(parent, 1, 2)
print("After union(1,2):", parent)

print("find(2):", find(parent, 2))  # Should return 0 (root parent)
