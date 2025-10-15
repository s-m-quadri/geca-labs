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

#solution
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(edges, V):
    edges = sorted(edges, key=lambda x: x[2])
    
    parent = [i for i in range(V)]
    mst = []
    total_weight = 0

    for u, v, w in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:  # No cycle formed
            union(parent, root_u, root_v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


# Example (very important)
edges = [
    (0, 1, 8),
    (0, 2, 5),
    (1, 2, 10),
    (1, 3, 2),
    (2, 3, 3),
    (2, 4, 7),
    (3, 4, 1)
]
V = 5

mst, weight = kruskal_mst(edges, V)
print("MST Edges:", mst)
print("Total Weight:", weight)

