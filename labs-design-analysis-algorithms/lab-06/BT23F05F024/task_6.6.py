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

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x == root_y:
        return False
    parent[root_y] = root_x
    return True

def kruskal_mst(edges, num_nodes):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(num_nodes)]
    mst_edges = []
    for u, v, w in edges:
        if union(parent, u, v):
            mst_edges.append((u, v, w))
    return mst_edges

def adjacency_list(mst_edges):
    adj = {}
    for u, v, _ in mst_edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
num_nodes = 4
mst = kruskal_mst(edges, num_nodes)
adj = adjacency_list(mst)

print("MST edges:", mst)
for k in adj:
    print(f"{k}: {adj[k]}")
