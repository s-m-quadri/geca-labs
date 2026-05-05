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
    return [i for i in range(n)]

def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return x

def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal(n, edges):
    parent = initialize_union_find(n)
    edges.sort(key=lambda x: x[2])
    mst = []
    total_weight = 0
    for u, v, w in edges:
        if union(u, v, parent):
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight


edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
n = 4
mst, weight = kruskal(n, edges)
print("MST edges:", mst)
print("Total weight:", weight)
