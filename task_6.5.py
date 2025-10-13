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

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, x, y):
    rx = find(p, x)
    ry = find(p, y)
    if rx != ry:
        p[ry] = rx
    return p

def kruskal(n, e):
    p = create_parent_array(n)
    mst = []
    tw = 0
    for u, v, w in sorted(e, key=lambda x: x[2]):
        if find(p, u) != find(p, v):
            union(p, u, v)
            mst.append((u, v, w))
            tw += w
    return mst, tw

n = 4
e = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
mst, w = kruskal(n, e)
print("MST edges:", mst)
print("Total MST weight:", w)
