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
import matplotlib.pyplot as plt
import networkx as nx       

def kruskal_mst(edges, num_vertices):   
    # Sort edges based on weight
    edges.sort(key=lambda x: x[2])
    
    # Initialize parent array for union-find
    parent = [i for i in range(num_vertices)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX  # Merge sets
    
    mst_edges = []
    total_weight = 0
    for u, v, w in edges:
        if find(u) != find(v):  # No cycle
            union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w
            
    return mst_edges, total_weight      

def build_adjacency_list(mst_edges):
    adj_list = {}
    for u, v, _ in mst_edges:
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list
def print_adjacency_list(adj_list):
    for node in sorted(adj_list):
        print(f"{node}: {adj_list[node]}")

def visualize_mst(mst_edges):
    G = nx.Graph()
    for u, v, w in mst_edges:
        G.add_edge(u, v, weight=w)
    
    pos = nx.spring_layout(G)
    weights = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
    
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()

# Example usage 
edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]     
num_vertices = 4
mst_edges, total_weight = kruskal_mst(edges, num_vertices)
print("MST edges:", mst_edges)
print("Total weight of MST:", total_weight)
adj_list = build_adjacency_list(mst_edges)
print("Adjacency List of MST:")
print_adjacency_list(adj_list)
# Optional visualization
visualize_mst(mst_edges)    
            


