def find(parent, x):
    """
    Recursively find the root parent of x.
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    """
    Merge the sets containing x and y.
    """
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root  # Make one root the parent of the other

# Example usage
parent = [0, 1, 2, 3]

union(parent, 0, 1)
print("Parent after union(0,1):", parent)
print("Find(1):", find(parent, 1))  # Should return 0

union(parent, 1, 2)
print("Parent after union(1,2):", parent)
print("Find(2):", find(parent, 2))  # Should return 0

union(parent, 2, 3)
print("Parent after union(2,3):", parent)
print("Find(3):", find(parent, 3))  # Should return 0
