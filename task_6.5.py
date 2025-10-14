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
def create_parent_array(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal(n, edges):
    parent = create_parent_array(n)
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst = []
    total_weight = 0

    for u, v, w in sorted_edges:
        if union(parent, u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


edges_input = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
num_vertices = 4
mst_edges, mst_weight = kruskal(num_vertices, edges_input)

print("MST Edges:", mst_edges)
print("Total Weight:", mst_weight)
