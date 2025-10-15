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
# Task 6.6: Challenge - Visualize MST
# -------------------------------------

def create_parent_array(num_vertices):
    return [i for i in range(num_vertices)]

def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        parent[root_y] = root_x

def kruskal_mst(edges, num_vertices):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    parent = create_parent_array(num_vertices)
    mst_edges = []
    total_weight = 0

    for u, v, w in sorted_edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            union(parent, root_u, root_v)
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight


def build_adjacency_list(mst_edges, num_vertices):
    adjacency_list = {i: [] for i in range(num_vertices)}

    for u, v, w in mst_edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    return adjacency_list


def visualize_mst(mst_edges):
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
    except ImportError:
        print("NetworkX or Matplotlib not installed. Skipping visualization.")
        return

    G = nx.Graph()
    G.add_weighted_edges_from(mst_edges)

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()


edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
num_vertices = 4

mst, total_weight = kruskal_mst(edges, num_vertices)
adj_list = build_adjacency_list(mst, num_vertices)

print("MST Edges:", mst)
print("Total Weight of MST:", total_weight)
print("\nAdjacency List Representation:")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

visualize_mst(mst)

