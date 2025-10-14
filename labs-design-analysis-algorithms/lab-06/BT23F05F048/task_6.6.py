# Task 6.6: Challenge - Visualize MST
# -------------------------------------
# Extend Kruskal’s algorithm:
# 1. Input edges and build MST.
# 2. Print MST edges in adjacency list format.
# 3. (Optional for extra) Use networkx + matplotlib to plot MST.

# Example:
# MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# Expected adjacency list:
# 0: [1, 3]
# 1: [0]
# 2: [3]
# 3: [0, 2]

# Hint: Use dictionary for adjacency list.
# Tip: Visualization part is optional, but fun for testing.

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
def mst_to_adj_list(mst):
    adj = {}
    for u, v, w in mst:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)
    return adj

n = 4
e = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
mst, w = kruskal(n, e)
print("MST edges:", mst)
print("Total MST weight:", w)   