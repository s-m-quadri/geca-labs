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
    parent = [i for i in range(V)]
    
    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst_edges = []
    mst_weight = 0
    
    for u, v, w in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
            mst_weight += w
    
    return mst_edges, mst_weight

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4
mst_edges, mst_weight = kruskal_mst(edges, V)

print("MST Edges:", mst_edges)
print("Total MST Weight:", mst_weight)
