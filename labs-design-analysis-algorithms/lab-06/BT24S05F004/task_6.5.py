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
# -------------------------------------------------

# Step 1: Initialize parent array
def create_parent(V):
    return [i for i in range(V)]

# Step 2: Find function (with path compression)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# Step 3: Union function
def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  # attach one tree under another

# Step 4: Kruskal’s MST function
def kruskal(V, edges):
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])

    parent = create_parent(V)
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        # If including this edge doesn’t cause a cycle
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight


# ✅ Example test case
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

V = 4
mst_edges, total_weight = kruskal(V, edges)

print("MST Edges:", mst_edges)
print("Total MST Weight:", total_weight)
