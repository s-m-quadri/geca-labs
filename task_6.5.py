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

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[yroot] = xroot

def kruskal(n, edges):
    parent = [i for i in range(n)]
    mst = []
    total_weight = 0
    sorted_edges = sorted(edges, key=lambda x: x[2])
    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

if __name__ == "__main__":
    edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    mst, weight = kruskal(4, edges)
    print("MST edges:", mst)
    print("MST weight:", weight)
