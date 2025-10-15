# Task 6.5: Building MST using Kruskal’s Algorithm
# -------------------------------------------------
# Write Kruskal’s algorithm using edges list and union-find.
# Iterate over sorted edges, add edge if it doesn’t form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.

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

def kruskals_mst(edges, num_vertices):
    """
    Build MST using Kruskal's algorithm.
    
    Args:
        edges: List of tuples (u, v, w)
        num_vertices: Number of vertices in the graph
    
    Returns:
        Tuple of (mst_edges, total_weight)
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize parent array
    parent = [i for i in range(num_vertices)]
    
    mst_edges = []
    total_weight = 0
    edges_added = 0
    
    # Process edges in order of weight
    for u, v, w in sorted_edges:
        # Check if adding this edge creates a cycle
        if union(parent, u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            edges_added += 1
            
            # MST has n-1 edges
            if edges_added == num_vertices - 1:
                break
    
    return mst_edges, total_weight

# Test the function
if __name__ == "__main__":
    edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    num_vertices = 4
    
    mst_edges, total_weight = kruskals_mst(edges, num_vertices)
    print("MST edges:", mst_edges)
    print("Total MST weight:", total_weight)
