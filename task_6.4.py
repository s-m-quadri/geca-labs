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
        parent[y_root] = x_root  # attach y's root to x's root
