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
# Task 6.5: Kruskal’s Algorithm for MST
# --------------------------------------

def create_parent(n):
    """Initialize parent array"""
    return [i for i in range(n)]

def find(parent, x):
    """Find the root parent of x"""
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    """Union of sets containing x and y"""
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(vertices, edges):
    """
    vertices: number of vertices
    edges: list of tuples (u, v, w)
    Returns: MST edges and total weight
    """
    # Step 1: Sort edges by weight
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Initialize Union-Find
    parent = create_parent(vertices)
    
    mst_edges = []
    total_weight = 0
    
    # Step 3: Iterate over sorted edges
    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):  # No cycle
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    
    return mst_edges, total_weight

# Example usage
vertices = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

mst_edges, mst_weight = kruskal_mst(vertices, edges)
print("MST edges:", mst_edges)
print("Total MST weight:", mst_weight)

