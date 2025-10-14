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
    # Initialize parent array: parent[i] = i
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] == x:
        return x
    else:
        return find(parent, parent[x])

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root

def kruskal_mst(vertices_count, edges):
    edges.sort(key=lambda x: x[2])
    
    parent = initialize_union_find(vertices_count)
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

if __name__ == "__main__":
    vertices_count = 4
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    
    mst_edges, mst_weight = kruskal_mst(vertices_count, edges)
    
    print("Edges in MST:", mst_edges)
    print("Total weight of MST:", mst_weight)
