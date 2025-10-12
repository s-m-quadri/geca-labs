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


def initialize_union_find(n):
    return [i for i in range(n)]

def find(parent, x):
    if parent[x] == x:
        return x
    else:
        return find(parent, parent[x])

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root != y_root:
        parent[y_root] = x_root

def kruskal_mst(vertices_count, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    parent = initialize_union_find(vertices_count)
    mst_edges = []
    total_weight = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight

def build_adjacency_list(vertices_count, mst_edges):
    adj_list = {i: [] for i in range(vertices_count)}
    for u, v, _ in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)  
    return adj_list

def visualize_mst(mst_edges):
    try:
        import networkx as nx
        import matplotlib.pyplot as plt

        G = nx.Graph()
        for u, v, w in mst_edges:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, font_size=12)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.title("MST Visualization")
        plt.show()
    except ImportError:
        print("Install networkx and matplotlib to visualize MST.")

if __name__ == "__main__":
    vertices_count = 4
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]

    mst_edges, mst_weight = kruskal_mst(vertices_count, edges)
    print("MST edges:", mst_edges)
    print("Total weight of MST:", mst_weight)

    adj_list = build_adjacency_list(vertices_count, mst_edges)
    print("Adjacency list of MST:")
    for vertex, neighbors in adj_list.items():
        print(f"{vertex}: {neighbors}")

    visualize_mst(mst_edges)
