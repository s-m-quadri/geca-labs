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
def create_parent(n):
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
    parent = create_parent(n)
    edges = sorted(edges, key=lambda x: x[2])
    mst = []
    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
    return mst

def build_adjacency_list(mst):
    adj = {}
    for u, v, _ in mst:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    return adj

edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst = kruskal(4, edges)
adj_list = build_adjacency_list(mst)
print("MST edges:", mst)
for node in adj_list:
    print(f"{node}: {adj_list[node]}")

#  visualization
# try:
#     import networkx as nx
#     import matplotlib.pyplot as plt
#     G = nx.Graph()
#     G.add_weighted_edges_from(mst)
#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10)
#     labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
#     plt.show()
# except ImportError:
#     pass
