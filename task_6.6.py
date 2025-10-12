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

import networkx as nx
import matplotlib.pyplot as plt

def kruskal_mst(edges, vertices):
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(vertices)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

def build_adjacency_list(mst_edges, vertices):
    adjacency_list = {i: [] for i in range(vertices)}
    for u, v, w in mst_edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list

def visualize_mst(mst_edges):
    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree")
    plt.show()

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
vertices = 4

mst_edges, mst_weight = kruskal_mst(edges, vertices)
print("MST edges:", mst_edges)
print("MST weight:", mst_weight)

adjacency_list = build_adjacency_list(mst_edges, vertices)
print("Adjacency List:")
for vertex, neighbors in adjacency_list.items():
    print(f"{vertex}: {neighbors}")

visualize_mst(mst_edges)