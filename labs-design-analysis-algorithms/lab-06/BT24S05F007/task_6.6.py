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

def build_mst_and_adj(edges):
    """
    Build MST using Kruskal (local implementation) and print adjacency list.
    edges: iterable of (u, v, w)
    """
    edges = list(edges)
    if not edges:
        print("No edges provided.")
        return [], {}

    # Kruskal (local)
    max_vertex = max(max(u, v) for u, v, _ in edges)
    parent = [i for i in range(max_vertex + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    sorted_edges = sorted(edges, key=lambda e: e[2])
    mst = []
    for u, v, w in sorted_edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    # build adjacency list
    adj = {}
    for u, v, _ in mst:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)

    # Ensure all vertices that appear in edges exist in adjacency (even if isolated in MST)
    vertices = set()
    for u, v, _ in edges:
        vertices.add(u)
        vertices.add(v)
    for x in vertices:
        adj.setdefault(x, [])

    # print adjacency list in sorted order
    for node in sorted(adj.keys()):
        print(f"{node}: {sorted(adj[node])}")

    return mst, adj

if __name__ == "__main__":
    example = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    mst, adj = build_mst_and_adj(example)
    # Optional visualization if networkx and matplotlib are available
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
        G = nx.Graph()
        for u, v, _ in mst:
            G.add_edge(u, v)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, edge_color="gray")
        plt.title("MST")
        plt.show()
    except Exception:
        pass
