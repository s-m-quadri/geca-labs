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

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root

def kruskal_mst(edges, V):
    edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(V)]
    mst_edges = []
    mst_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            mst_weight += w

    return mst_edges, mst_weight

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4
mst_edges, mst_weight = kruskal_mst(edges, V)
print("MST edges:", mst_edges)
print("MST weight:", mst_weight)
