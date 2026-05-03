def find(parent, x):
    """
    Recursively find root parent of x.
    """
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    """
    Merge sets containing x and y.
    """
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root

def kruskal_mst(edges, V):
    """
    Build MST using Kruskal's algorithm.

    edges: list of tuples (u, v, w)
    V: number of vertices
    Returns: (mst_edges, total_weight)
    """
    # Step 1: Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Step 2: Initialize union-find parent array
    parent = [i for i in range(V)]

    mst_edges = []
    total_weight = 0

    # Step 3: Iterate over sorted edges
    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):  # If adding edge does not form a cycle
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

# Test case
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4

mst_edges, mst_weight = kruskal_mst(edges, V)
print("MST edges:", mst_edges)
print("MST total weight:", mst_weight)
