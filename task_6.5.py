# Task 6.5: Building MST using Kruskal's Algorithm
# -------------------------------------------------
# Write Kruskal's algorithm using edges list and union-find.
# Iterate over sorted edges, add edge if it doesn't form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.

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
    """
    Kruskal's algorithm to find MST.
    
    Args:
        edges: List of tuples (u, v, weight)
        num_vertices: Number of vertices in graph
    
    Returns:
        Tuple of (mst_edges, total_weight)
    """
    # Sort edges by weight
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize union-find
    parent = list(range(num_vertices))
    
    mst_edges = []
    total_weight = 0
    
    for u, v, weight in sorted_edges:
        # Check if adding this edge creates a cycle
        if union(parent, u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            
            # Stop when we have n-1 edges
            if len(mst_edges) == num_vertices - 1:
                break
    
    return mst_edges, total_weight

# Test the algorithm
if __name__ == "__main__":
    # Test case from example
    edges = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
    num_vertices = 4
    
    mst_edges, total_weight = kruskal_mst(edges, num_vertices)
    
    print("Original edges:", edges)
    print("MST edges:", mst_edges)
    print("Total MST weight:", total_weight)