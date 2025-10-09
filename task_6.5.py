# Task 6.5: Building MST using Kruskal's Algorithm
# -------------------------------------------------
# Write Kruskal's algorithm using edges liprint(f"Edge match: {actual_edges_set.issubset(expected_edges_set) or actual_edges_set == expected_edges_set}")find.
# Iterate over sorted edges, add edge if it doesn't form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.

def find(parent, x):
    """Find root of x with path compression."""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    """Union by rank for better performance."""
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    return False

def kruskals_algorithm(vertices, edges):
    """
    Implement Kruskal's algorithm to find Minimum Spanning Tree.
    
    Args:
        vertices: number of vertices in graph
        edges: list of tuples (u, v, weight)
    
    Returns:
        tuple: (mst_edges, total_weight)
    """
    mst_edges = []
    total_weight = 0
    
    parent = list(range(vertices))
    rank = [0] * vertices
    
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    print("Kruskal's Algorithm Steps:")
    print(f"Sorted edges: {sorted_edges}")
    print()
    
    for i, (u, v, weight) in enumerate(sorted_edges):
        print(f"Step {i+1}: Considering edge ({u}, {v}) with weight {weight}")
        
        if find(parent, u) != find(parent, v):
            if union(parent, rank, u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                print(f"  → Added to MST. Total weight: {total_weight}")
                
                if len(mst_edges) == vertices - 1:
                    print(f"  → MST complete with {vertices-1} edges!")
                    break
        else:
            print(f"  → Rejected (would create cycle)")
        print()
    
    return mst_edges, total_weight

def display_mst_result(mst_edges, total_weight, title="MST Result"):
    """Display the MST result in a formatted way."""
    print("="*50)
    print(title)
    print("="*50)
    print(f"MST Edges: {mst_edges}")
    print(f"Total Weight: {total_weight}")
    print(f"Number of edges: {len(mst_edges)}")
    print()

def create_adjacency_matrix_to_edges(adj_matrix):
    """Convert adjacency matrix to edge list."""
    edges = []
    n = len(adj_matrix)
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i][j] != 0:
                edges.append((i, j, adj_matrix[i][j]))
    return edges

print("Test Case 1 - Given example:")
edges1 = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges1, total_weight1 = kruskals_algorithm(4, edges1)
display_mst_result(mst_edges1, total_weight1, "Test Case 1 Result")

print("Test Case 2 - Complete graph with 5 vertices:")
edges2 = [
    (0,1,2), (0,2,3), (0,3,3), (0,4,6),
    (1,2,4), (1,3,2), (1,4,3),
    (2,3,1), (2,4,1),
    (3,4,5)
]
mst_edges2, total_weight2 = kruskals_algorithm(5, edges2)
display_mst_result(mst_edges2, total_weight2, "Test Case 2 Result")

print("Test Case 3 - From adjacency matrix:")
adj_matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

edges3 = create_adjacency_matrix_to_edges(adj_matrix)
print(f"Converted {len(edges3)} edges from adjacency matrix:")
for edge in edges3:
    print(f"  {edge}")
print()

mst_edges3, total_weight3 = kruskals_algorithm(9, edges3)
display_mst_result(mst_edges3, total_weight3, "Test Case 3 Result")

print("Test Case 4 - Disconnected graph:")
edges4 = [(0,1,1), (1,2,2), (3,4,3), (4,5,4)]
print("Testing disconnected graph (two components):")
mst_edges4, total_weight4 = kruskals_algorithm(6, edges4)
display_mst_result(mst_edges4, total_weight4, "Test Case 4 Result")
print(f"Note: Only {len(mst_edges4)} edges found (should be 5 for connected graph)")

print("Verification of expected results:")
print("Expected for Test Case 1: [(2,3,4), (0,3,5), (0,1,10)], weight = 19")
print(f"Actual result: {mst_edges1}, weight = {total_weight1}")
print(f"Match: {total_weight1 == 19}")

expected_edges_set = {(2,3,4), (0,3,5), (0,1,10), (3,2,4), (3,0,5), (1,0,10)}
actual_edges_set = {(min(u,v), max(u,v), w) for u,v,w in mst_edges1}
print(f"Edge match: {actual_edges_set.issubset(expected_edges_set) or actual_edges_set == expected_edges_set}")
#Building MST using Kruskal’s Algorithm
# -------------------------------------------------
# Write Kruskal’s algorithm using edges list and union-find.
# Iterate over sorted edges, add edge if it doesn’t form a cycle.

# Example:
# Graph: [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
# Expected MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# MST weight = 19

# Hint: Use union-find to check cycle.
# Tip: Keep track of total weight and chosen edges.
