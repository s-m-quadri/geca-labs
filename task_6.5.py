def kruskal_mst(edges, V):
    """
    edges: list of tuples (u, v, w)
    V: number of vertices
    Returns: list of MST edges and total weight
    """
    # Step 1: Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Step 2: Initialize union-find
    parent = [i for i in range(V)]

    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root

    mst_edges = []
    total_weight = 0

    # Step 3: Iterate over sorted edges
    for u, v, w in sorted_edges:
        if find(u) != find(v):  # No cycle
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

