def kruskal_mst_adjacency(edges, V):
    """
    Build MST using Kruskal's algorithm and return adjacency list.
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # Initialize union-find
    parent = [i for i in range(V)]
    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])
    
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            parent[y_root] = x_root

    # Build MST
    mst_edges = []
    for u, v, w in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v, w))

    # Create adjacency list
    adj_list = {i: [] for i in range(V)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # Undirected

    return mst_edges, adj_list

# Optional visualization
def plot_mst(adj_list, mst_edges):
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
    except ImportError:
        print("networkx or matplotlib not installed. Skipping plot.")
        return

    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    edge_labels = {(u, v): w for u, v, w in mst_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Kruskal MST")
    plt.show()

