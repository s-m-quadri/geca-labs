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
# kruskal_mst.py
# Task 6.5: Building MST using Kruskal's Algorithm

def find(parent, x):
    """Find root parent of x"""
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def union(parent, x, y):
    """Union sets containing x and y"""
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x


def kruskal_mst(vertices, edges):
    """
    Build MST using Kruskal's algorithm.
    
    Parameters:
    - vertices: number of vertices
    - edges: list of tuples (u, v, w)
    
    Returns:
    - mst_edges: list of edges included in MST
    - total_weight: sum of MST edge weights
    """
    # Step 1: Sort edges by weight
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Initialize union-find parent array
    parent = [i for i in range(vertices)]
    
    mst_edges = []
    total_weight = 0
    
    # Step 3: Iterate over edges
    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    
    return mst_edges, total_weight


# Example usage
vertices = 4
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, mst_weight = kruskal_mst(vertices, edges)

print("Edges in MST:")
for u, v, w in mst_edges:
    print(f"{u} -- {v} : {w}")
print(f"Total weight of MST: {mst_weight}")
