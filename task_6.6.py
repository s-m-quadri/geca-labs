# Task 6.6: Challenge - Visualize MST
# -------------------------------------
# Extend Kruskal's algorithm:
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
    """Find root parent of x."""
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, x, y):
    """Union two sets containing x and y."""
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x
        return True
    return False

def kruskal_mst(edges, num_vertices):
    """Kruskal's algorithm to find MST."""
    sorted_edges = sorted(edges, key=lambda x: x[2])
    parent = list(range(num_vertices))
    
    mst_edges = []
    total_weight = 0
    
    for u, v, weight in sorted_edges:
        if union(parent, u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            if len(mst_edges) == num_vertices - 1:
                break
    
    return mst_edges, total_weight

def mst_to_adjacency_list(mst_edges, num_vertices):
    """Convert MST edges to adjacency list representation."""
    adj_list = {i: [] for i in range(num_vertices)}
    
    for u, v, weight in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return adj_list

def visualize_mst(edges, num_vertices):
    """
    Build MST and display as adjacency list.
    Optionally plot if networkx and matplotlib are available.
    """
    # Build MST
    mst_edges, total_weight = kruskal_mst(edges, num_vertices)
    
    # Convert to adjacency list
    adj_list = mst_to_adjacency_list(mst_edges, num_vertices)
    
    print("MST edges:", mst_edges)
    print("Total MST weight:", total_weight)
    print("\nAdjacency list representation:")
    for vertex in sorted(adj_list.keys()):
        print(f"{vertex}: {adj_list[vertex]}")
    
    # Optional: Try to plot using networkx and matplotlib
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
        
        # Create graph
        G = nx.Graph()
        for u, v, weight in mst_edges:
            G.add_edge(u, v, weight=weight)
        
        # Plot
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=500, font_size=16, font_weight='bold')
        
        # Draw edge labels
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        
        plt.title("Minimum Spanning Tree")
        plt.show()
        
    except ImportError:
        print("\nNote: Install networkx and matplotlib for visualization:")
        print("pip install networkx matplotlib")

# Test the visualization
if __name__ == "__main__":
    # Test case
    edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    num_vertices = 4
    
    print("Original edges:", edges)
    visualize_mst(edges, num_vertices)
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
