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
    """Find root parent with path compression."""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    """Union two sets."""
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_x] = root_y
        return True
    return False

def kruskals_mst_with_adjacency(edges, num_vertices):
    """
    Build MST using Kruskal's algorithm and return adjacency list.
    
    Args:
        edges: List of tuples (u, v, w)
        num_vertices: Number of vertices in the graph
    
    Returns:
        Tuple of (mst_edges, adjacency_list, total_weight)
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize parent array
    parent = [i for i in range(num_vertices)]
    
    mst_edges = []
    total_weight = 0
    edges_added = 0
    
    # Initialize adjacency list
    adjacency_list = {i: [] for i in range(num_vertices)}
    
    # Process edges in order of weight
    for u, v, w in sorted_edges:
        # Check if adding this edge creates a cycle
        if union(parent, u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            edges_added += 1
            
            # Add to adjacency list (undirected graph)
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            
            # MST has n-1 edges
            if edges_added == num_vertices - 1:
                break
    
    return mst_edges, adjacency_list, total_weight

def print_adjacency_list(adjacency_list):
    """Print adjacency list in a formatted way."""
    for vertex in sorted(adjacency_list.keys()):
        print(f"{vertex}: {adjacency_list[vertex]}")

def visualize_mst(mst_edges, num_vertices):
    """Optional: Visualize MST using networkx and matplotlib."""
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
        
        # Create graph
        G = nx.Graph()
        
        # Add vertices
        G.add_nodes_from(range(num_vertices))
        
        # Add MST edges
        for u, v, w in mst_edges:
            G.add_edge(u, v, weight=w)
        
        # Draw graph
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 8))
        
        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=500, font_size=16, font_weight='bold')
        
        # Draw edge labels (weights)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        
        plt.title("Minimum Spanning Tree")
        plt.axis('off')
        plt.show()
        
    except ImportError:
        print("NetworkX and/or Matplotlib not available for visualization.")
        print("Install with: pip install networkx matplotlib")

# Test the function
if __name__ == "__main__":
    # Test with the example from task 6.5
    edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    num_vertices = 4
    
    mst_edges, adjacency_list, total_weight = kruskals_mst_with_adjacency(edges, num_vertices)
    
    print("MST edges:", mst_edges)
    print("Total MST weight:", total_weight)
    print("\nAdjacency list representation:")
    print_adjacency_list(adjacency_list)
    
    # Optional visualization
    print("\nAttempting to visualize MST...")
    visualize_mst(mst_edges, num_vertices)
