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


# ---------- Helper Functions (Union-Find) ----------
def create_parent_array(n):
    return [i for i in range(n)]

def find(parent, x):
    # Recursively find root parent
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x  # merge sets


# ---------- Kruskal’s Algorithm ----------
def kruskal(n, edges):
    # Sort edges by weight
    edges = sorted(edges, key=lambda x: x[2])
    
    parent = create_parent_array(n)
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        # Find roots of u and v
        root_u = find(parent, u)
        root_v = find(parent, v)

        # If different roots, no cycle → add edge
        if root_u != root_v:
            union(parent, root_u, root_v)
            mst_edges.append((u, v, w))
            total_weight += w

    print("MST Edges:", mst_edges)
    print("Total MST Weight:", total_weight)

    return mst_edges, total_weight


# ---------- Example Usage ----------
edges_input = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(4, edges_input)
