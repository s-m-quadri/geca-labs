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
def kruskal_mst(edges, num_vertices):
    """
    edges: list of (u, v, w)
    num_vertices: total number of vertices
    """
    # Step 1: Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Step 2: Initialize Union-Find parent array
    parent = [i for i in range(num_vertices)]
    
    # Step 3: Helper functions
    def find(x):
        if parent[x] == x:
            return x
        else:
            return find(parent, parent[x])
    
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root
    
    # Step 4: Kruskal's algorithm
    mst_edges = []
    total_weight = 0
    for u, v, w in sorted_edges:
        if find(u) != find(v):  # No cycle
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    
    return mst_edges, total_weight

# Example usage
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
num_vertices = 4
mst, weight = kruskal_mst(edges, num_vertices)

print("MST edges:", mst)
print("Total MST weight:", weight)
