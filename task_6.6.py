import networkx as nx
import matplotlib.pyplot as plt

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root

def kruskal_mst(edges, V):
    """Build MST using Kruskal's algorithm."""
    sorted_edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(V)]
    mst_edges = []

    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
    return mst_edges

def mst_to_adjacency_list(mst_edges, V):
    """Convert MST edges to adjacency list format."""
    adj_list = {i: [] for i in range(V)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Undirected graph
    return adj_list

def visualize_mst(mst_edges, V):
    """Visualize MST using networkx."""
    G = nx.Graph()
    G.add_nodes_from(range(V))
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Test case
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
V = 4

mst_edges = kruskal_mst(edges, V)
adj_list = mst_to_adjacency_list(mst_edges, V)

print("MST edges:", mst_edges)
print("Adjacency list:")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")

# Optional: visualize the MST
visualize_mst(mst_edges, V)
