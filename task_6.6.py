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

def kruskal_mst_adjacency(edges, V):
    edges_sorted = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(V)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root

    mst_edges = []
    for u, v, w in edges_sorted:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))

    adj_list = {i: [] for i in range(V)}
    for u, v, w in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return mst_edges, adj_list

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, adj_list = kruskal_mst_adjacency(edges, 4)

print("MST edges:", mst_edges)
print("Adjacency list:")
for key in adj_list:
    print(f"{key}: {adj_list[key]}")
