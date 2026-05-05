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
def kruskal_mst_with_adj_list(edges, V):
    parent = [i for i in range(V)]
    
    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst_edges = []
    
    for u, v, w in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
    
    # Build adjacency list
    adj_list = {i: [] for i in range(V)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return mst_edges, adj_list

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4
mst_edges, adj_list = kruskal_mst_with_adj_list(edges, V)

print("MST Edges:", mst_edges)
print("Adjacency List:")
for key in adj_list:
    print(f"{key}: {adj_list[key]}")

# Optional visualization
try:
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    G.add_edges_from([(u, v) for u, v, _ in mst_edges])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700)
    labels = {(u, v): w for u, v, w in mst_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
except ImportError:
    print("Install networkx and matplotlib to see visualization.")
