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

def make_parent(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal(n, edges):
    edges = sorted(edges, key=lambda x: x[2])
    parent = make_parent(n)
    mst = []
    total_weight = 0
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, mst_weight = kruskal(4, edges)
print(mst_edges)
print(mst_weight)
