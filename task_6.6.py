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
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[yroot] = xroot

def kruskal(n, edges):
    parent = [i for i in range(n)]
    sorted_edges = sorted(edges, key=lambda x: x[2])
    mst_edges = []
    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
    return mst_edges

def build_adjacency_list(mst_edges, n):
    adj = {i: [] for i in range(n)}
    for u, v, _ in mst_edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

if __name__ == "__main__":
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    n = 4
    mst = kruskal(n, edges)
    print("MST edges:", mst)
    adj = build_adjacency_list(mst, n)
    print("Adjacency list:")
    for node in adj:
        print(f"{node}: {adj[node]}")

# Optional: Visualization (requires networkx and matplotlib)
try:
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.Graph()
    for u, v, w in mst:
        G.add_edge(u, v, weight=w)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("MST Visualization")
    plt.show()
except ImportError:
    pass
