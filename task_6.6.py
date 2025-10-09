# Task 6.6: Visualize MST
# ------------------------

import networkx as nx
import matplotlib.pyplot as plt

def initialize_parent(V):
    return [i for i in range(V)]

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(V, edges):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    parent = initialize_parent(V)
    mst_edges = []
    total_weight = 0
    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    return mst_edges, total_weight

def build_adjacency_list(V, mst_edges):
    """Convert MST edges to adjacency list format"""
    adj_list = {i: [] for i in range(V)}
    for u, v, w in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # undirected graph
    return adj_list

def plot_mst(V, mst_edges):
    """Optional: Visualize MST using networkx and matplotlib"""
    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)  # layout for visualization
    edge_labels = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()


# Example Test
V = 4
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges, mst_weight = kruskal_mst(V, edges)

print("MST Edges:", mst_edges)
print("MST Total Weight:", mst_weight)

adj_list = build_adjacency_list(V, mst_edges)
print("\nMST Adjacency List:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

# Optional: Plot MST
plot_mst(V, mst_edges)
