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

def initialize_union_find(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])  # No path compression

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False  # Already in the same set (would form cycle)

def kruskal_mst(edges, num_vertices):
    """
    Kruskal's algorithm to find the Minimum Spanning Tree (MST)

    Parameters:
    edges (list of tuples): Each tuple is (u, v, weight)
    num_vertices (int): Number of vertices in the graph

    Returns:
    tuple: (MST_edges, total_weight)
    """
    # Step 1: Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Step 2: Initialize Union-Find
    parent = initialize_union_find(num_vertices)

    # Step 3: Iterate and build MST
    mst = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if union(parent, u, v):  # If u and v are not connected
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight
