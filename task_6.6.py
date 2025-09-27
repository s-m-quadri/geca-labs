## Task 6.6: Challenge - Visualize MST
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
# Kruskal MST with Union-Find
def kruskal_mst(edges, V):
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]
    
    def union(parent, x, y):
        x_root = find(parent, x)
        y_root = find(parent, y)
        if x_root != y_root:
            parent[y_root] = x_root
    
    parent = [i for i in range(V)]
    mst_edges = []
    edges = sorted(edges, key=lambda x: x[2])
    
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
    return mst_edges

def build_adj_list(mst_edges):
    adj = {}
    for u, v, _ in mst_edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj

# Example usage
edges = [(0,1,10),(0,3,5),(2,3,4)]
V = 4
mst_edges = kruskal_mst(edges, V)
adj_list = build_adj_list(mst_edges)

print("Adjacency list:")
for node in sorted(adj_list):
    print(f"{node}: {adj_list[node]}")
