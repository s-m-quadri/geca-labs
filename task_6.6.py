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
def make_parent(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal(n, edges):
    parent = make_parent(n)
    mst = []
    edges_sorted = sorted(edges, key=lambda x: x[2])
    
    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
    
    return mst

def mst_to_adj_list(mst):
    adj = {}
    for u, v, _ in mst:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj

edges = [(]()
