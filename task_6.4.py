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
    Recursively find the root parent of x.
    """
    if parent[x] == x:
        return x
    else:
        return find(parent, parent[x])

def union(parent, x, y):
    """
    Merge sets containing x and y.
    """
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root  

# Example 
parent = [0, 1, 2, 3]


union(parent, 0, 1)
print("Parent after union(0,1):", parent)
union(parent, 1, 2)
print("Parent after union(1,2):", parent)


print("find(1):", find(parent, 1))  
print("find(2):", find(parent, 2))  

