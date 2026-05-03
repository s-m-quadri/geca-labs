# Task 6.5: Kruskal's MST Algorithm
# ---------------------------------

def initialize_parent(V):
    """Initialize parent array for Union-Find"""
    return [i for i in range(V)]

def find(parent, x):
    """Recursively find the root parent of x"""
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    """Union two sets containing x and y"""
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(V, edges):
    """
    Build MST using Kruskal's algorithm.
    
    Parameters:
        V : int
            Number of vertices
        edges : list of tuples
            Each tuple is (u, v, w)
    
    Returns:
        mst_edges : list of tuples
            Edges included in MST
        total_weight : int
            Total weight of MST
    """
    # Step 1: Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Initialize union-find parent array
    parent = initialize_parent(V)
    
    mst_edges = []
    total_weight = 0
    
    # Step 3: Iterate over edges
    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):  # no cycle
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    
    return mst_edges, total_weight


# Example Test
V = 4
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, mst_weight = kruskal_mst(V, edges)

print("MST Edges:", mst_edges)
print("MST Total Weight:", mst_weight)
