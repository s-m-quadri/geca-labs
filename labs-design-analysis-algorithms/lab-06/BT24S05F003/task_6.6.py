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
# mst_visualization.py
# Task 6.6: Visualize MST (Adjacency List + Optional Plot)

def find(parent, x):
    """Find root parent of x"""
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    """Union sets containing x and y"""
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(vertices, edges):
    """Return MST edges using Kruskal's algorithm"""
    edges_sorted = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(vertices)]
    
    mst_edges = []
    for u, v, w in edges_sorted:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
    return mst_edges

def mst_to_adjacency_list(vertices, mst_edges):
    """Convert MST edges to adjacency list"""
    adj_list = {i: [] for i in range(vertices)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  # undirected graph
    return adj_list

# Example usage
vertices = 4
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]

mst_edges = kruskal_mst(vertices, edges)
adj_list = mst_to_adjacency_list(vertices, mst_edges)

print("MST edges:")
for u, v, w in mst_edges:
    print(f"{u} -- {v} : {w}")

print("\nAdjacency List of MST:")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")

# Optional: Visualization using networkx
try:
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("MST Visualization")
    plt.show()
except ImportError:
    print("\nOptional visualization skipped. Install networkx and matplotlib to see MST plot.")
