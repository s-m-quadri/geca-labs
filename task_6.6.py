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
def initialize_union_find(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root

def kruskal_mst(edges, n_vertices):
    edges_sorted = sorted(edges, key=lambda x: x[2])
    parent = initialize_union_find(n_vertices)
    mst = []
    total_weight = 0

    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight

def mst_to_adjacency_list(mst_edges, n_vertices):
    adj_list = {i: [] for i in range(n_vertices)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
n_vertices = 4
mst_edges, mst_weight = kruskal_mst(edges, n_vertices)
adj_list = mst_to_adjacency_list(mst_edges, n_vertices)

print("MST edges:", mst_edges)
print("Total MST weight:", mst_weight)
print("Adjacency list of MST:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

# Optional visualization
try:
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_weighted_edges_from(mst_edges)
    pos = nx.spring_layout(G)
    n
