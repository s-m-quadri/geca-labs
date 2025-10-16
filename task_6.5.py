# Task 6.5: Building MST using Kruskal’s Algorithm
# -------------------------------------------------
# Write Kruskal’s algorithm using edges list and union-find.
# Iterate over sorted edges, add edge if it doesn’t form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.
def kruskal_mst(edges, V):
    """
    edges: list of tuples (u, v, w)
    V: number of vertices
    Returns: list of MST edges and total weight
    """
    # Step 1: Sort edges by weight
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Initialize Union-Find
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
    for u, v, w in edges_sorted:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    
    return mst_edges, total_weight

# Example usage
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4

mst_edges, mst_weight = kruskal_mst(edges, V)
print("MST edges:", mst_edges)     # Expected: [(2,3,4), (0,3,5), (0,1,10)]
print("MST total weight:", mst_weight)  # Expected: 19
