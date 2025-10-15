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
        return find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal_mst(num_vertices, edges):
    edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(num_vertices)]
    mst_edges = []
    for u, v, w in edges:
        if union(parent, u, v):
            mst_edges.append((u, v, w))
            if len(mst_edges) == num_vertices - 1:
                break
    return mst_edges

def build_adjacency_list(num_vertices, mst_edges):
    adj = {i: [] for i in range(num_vertices)}
    for u, v, _ in mst_edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

# Example usage:
if __name__ == "__main__":
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    num_vertices = 4
    mst_edges = kruskal_mst(num_vertices, edges)
    print("MST edges:", mst_edges)
    adj = build_adjacency_list(num_vertices, mst_edges)
    print("Adjacency list:")
    for node in adj:
        print(f"{node}: {adj[node]}")

    # Optional: Visualization
    try:
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph()
        for u, v, w in mst_edges:
            G.add_edge(u, v, weight=w)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("MST Visualization")
        plt.show()
    except ImportError:
        print("networkx or matplotlib not installed. Skipping visualization.")
