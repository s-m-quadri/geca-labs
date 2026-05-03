"""
Background:
Repeating iterations completes the MST construction.

Task:
Implement full Prim's algorithm for a given adjacency matrix.

Instruction:
- Input: adjacency matrix graph, start vertex.
- Output: list of MST edges (parent, vertex, weight).

Tip:
Use previous helper functions: min-key selection, key updates.

Test case:
graph = [
 [0, 2, 0, 6],
 [2, 0, 3, 8],
 [0, 3, 0, 0],
 [6, 8, 0, 0]
]
start = 0
# Expected MST edges: [(0,1,2),(1,2,3),(0,3,6)]
"""
def find_min_key_vertex(key, mstSet):
    """Find the vertex with minimum key value that is not yet in MST."""
    min_key = float('inf')
    min_index = -1

    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_key:
            min_key = key[v]
            min_index = v

    return min_index

def update_neighbors(graph, u, key, parent, mstSet):
    """Update key[] and parent[] arrays for neighbors of selected vertex u."""
    V = len(graph)

    for v in range(V):
        if (not mstSet[v] and 
            graph[u][v] > 0 and 
            graph[u][v] < key[v]):
            key[v] = graph[u][v]
            parent[v] = u

def prim_mst(graph, start=0):
    """
    Implement full Prim's algorithm to find Minimum Spanning Tree.
    
    Args:
        graph: Adjacency matrix representation of the graph
        start: Starting vertex (default is 0)
    
    Returns:
        list: List of MST edges as tuples (parent, vertex, weight)
    """
    V = len(graph)  # Number of vertices

    # Initialize arrays
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V

    # Start with the given starting vertex
    key[start] = 0

    mst_edges = []

    # Build MST with V-1 edges
    for _ in range(V):
        # Find vertex with minimum key not yet in MST
        u = find_min_key_vertex(key, mstSet)

        # If no vertex found, graph might be disconnected
        if u == -1:
            break

        # Add vertex to MST
        mstSet[u] = True

        # Add edge to MST (except for the starting vertex)
        if parent[u] != -1:
            weight = graph[parent[u]][u]
            mst_edges.append((parent[u], u, weight))

        # Update keys of neighbors
        update_neighbors(graph, u, key, parent, mstSet)

    return mst_edges

# Test the function
if __name__ == "__main__":
    # Test case from the problem
    graph = [
        [0, 2, 0, 6],
        [2, 0, 3, 8],
        [0, 3, 0, 0],
        [6, 8, 0, 0]
    ]
    start = 0

    print("Graph adjacency matrix:")
    for i, row in enumerate(graph):
        print(f"  {i}: {row}")

    mst_edges = prim_mst(graph, start)

    print(f"\nMST edges starting from vertex {start}:")
    total_weight = 0
    for parent, vertex, weight in mst_edges:
        print(f"  ({parent}, {vertex}, {weight})")
        total_weight += weight

    print(f"\nTotal MST weight: {total_weight}")

    # Expected: [(0,1,2),(1,2,3),(0,3,6)]
    expected_edges = [(0, 1, 2), (1, 2, 3), (0, 3, 6)]

    # Sort both lists for comparison (order might vary)
    mst_edges_sorted = sorted(mst_edges)
    expected_edges_sorted = sorted(expected_edges)

    print(f"\nExpected edges: {expected_edges_sorted}")
    print(f"Actual edges:   {mst_edges_sorted}")

    assert mst_edges_sorted == expected_edges_sorted, f"Expected {expected_edges_sorted}, got {mst_edges_sorted}"