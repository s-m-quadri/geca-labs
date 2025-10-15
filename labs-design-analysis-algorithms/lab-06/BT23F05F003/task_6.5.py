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
    edges_sorted = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(V)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root

    mst_edges = []
    total_weight = 0

    for u, v, w in edges_sorted:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, mst_weight = kruskal_mst(edges, 4)
print("MST edges:", mst_edges)
print("MST total weight:", mst_weight)
