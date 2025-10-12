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
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(edges, V):
    edges.sort(key=lambda x: x[2]) 
    parent = [i for i in range(V)]
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

def build_adjacency_list(mst_edges, V):
    adj_list = {i: [] for i in range(V)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

edges = [
    (0, 1, 4),
    (0, 3, 5),
    (1, 3, 6),
    (1, 2, 10),
    (2, 3, 4)
]
V = 4

mst_edges, total_weight = kruskal_mst(edges, V)
adj_list = build_adjacency_list(mst_edges, V)

print("MST Edges:", mst_edges)
print("Total Weight:", total_weight)
print("Adjacency List:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")