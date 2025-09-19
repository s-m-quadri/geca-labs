"""
Background:
Prim's algorithm can be optimized using priority queues.

Task:
Implement MST construction using a min-heap (heapq) to pick min-key vertex efficiently.

Instruction:
- Input: adjacency matrix or adjacency list.
- Output: MST edges with weights.
- Do not use linear search for min-key.

Tip:
Use heapq to maintain (key, vertex). Update keys carefully when a better edge is found.

Test case:
graph = [
 [0, 2, 0, 6, 0],
 [2, 0, 3, 8, 5],
 [0, 3, 0, 0, 7],
 [6, 8, 0, 0, 9],
 [0, 5, 7, 9, 0]
]
start = 0
# Expected MST edges: [(0,1,2),(1,2,3),(1,4,5),(0,3,6)]
"""

import heapq

def prim_mst_optimized(graph, start=0):
    """
    Implement Prim's algorithm using min-heap for efficiency.
    
    Args:
        graph: Adjacency matrix representation of the graph
        start: Starting vertex (default is 0)
    
    Returns:
        list: List of MST edges as tuples (parent, vertex, weight)
    """
    V = len(graph)  # Number of vertices
    
    # Track which vertices are in MST
    in_mst = [False] * V
    
    # Store parent information for MST construction
    parent = [-1] * V
    
    # Min-heap to store (key, vertex) pairs
    min_heap = [(0, start)]  # Start with (key=0, vertex=start)
    
    # Track minimum key values to avoid duplicate processing
    key = [float('inf')] * V
    key[start] = 0
    
    mst_edges = []
    
    while min_heap:
        # Extract vertex with minimum key
        current_key, u = heapq.heappop(min_heap)
        
        # Skip if vertex is already in MST or if this is an outdated entry
        if in_mst[u] or current_key > key[u]:
            continue
        
        # Add vertex to MST
        in_mst[u] = True
        
        # Add edge to MST (except for starting vertex)
        if parent[u] != -1:
            weight = graph[parent[u]][u]
            mst_edges.append((parent[u], u, weight))
        
        # Update keys of adjacent vertices
        for v in range(V):
            # Check if there's an edge and vertex v is not in MST
            if graph[u][v] > 0 and not in_mst[v]:
                # If we found a better path to vertex v
                if graph[u][v] < key[v]:
                    key[v] = graph[u][v]
                    parent[v] = u
                    # Push the updated key to heap
                    heapq.heappush(min_heap, (key[v], v))
    
    return mst_edges

def prim_mst_adjacency_list(adj_list, start=0):
    """
    Prim's algorithm with adjacency list representation.
    
    Args:
        adj_list: List of lists, where adj_list[u] contains (vertex, weight) pairs
        start: Starting vertex
    
    Returns:
        list: List of MST edges as tuples (parent, vertex, weight)
    """
    V = len(adj_list)
    in_mst = [False] * V
    parent = [-1] * V
    key = [float('inf')] * V
    key[start] = 0
    
    min_heap = [(0, start)]
    mst_edges = []
    
    while min_heap:
        current_key, u = heapq.heappop(min_heap)
        
        if in_mst[u] or current_key > key[u]:
            continue
        
        in_mst[u] = True
        
        if parent[u] != -1:
            # Find the weight of edge (parent[u], u)
            weight = current_key
            mst_edges.append((parent[u], u, weight))
        
        # Update adjacent vertices
        for v, weight in adj_list[u]:
            if not in_mst[v] and weight < key[v]:
                key[v] = weight
                parent[v] = u
                heapq.heappush(min_heap, (weight, v))
    
    return mst_edges

def adjacency_matrix_to_list(matrix):
    """Convert adjacency matrix to adjacency list."""
    V = len(matrix)
    adj_list = [[] for _ in range(V)]
    
    for u in range(V):
        for v in range(V):
            if matrix[u][v] > 0:
                adj_list[u].append((v, matrix[u][v]))
    
    return adj_list

# Test the function
if __name__ == "__main__":
    # Test case from the problem
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]
    start = 0
    
    print("Graph adjacency matrix:")
    for i, row in enumerate(graph):
        print(f"  {i}: {row}")
    
    # Test with adjacency matrix
    mst_edges = prim_mst_optimized(graph, start)
    
    print(f"\nMST edges (optimized with heap) starting from vertex {start}:")
    total_weight = 0
    for parent, vertex, weight in mst_edges:
        print(f"  ({parent}, {vertex}, {weight})")
        total_weight += weight
    
    print(f"\nTotal MST weight: {total_weight}")
    
    # Test with adjacency list
    adj_list = adjacency_matrix_to_list(graph)
    print(f"\nAdjacency list representation:")
    for i, neighbors in enumerate(adj_list):
        print(f"  {i}: {neighbors}")
    
    mst_edges_adj_list = prim_mst_adjacency_list(adj_list, start)
    print(f"\nMST edges (adjacency list) starting from vertex {start}:")
    for parent, vertex, weight in mst_edges_adj_list:
        print(f"  ({parent}, {vertex}, {weight})")
    
    # Expected: [(0,1,2),(1,2,3),(1,4,5),(0,3,6)]
    expected_edges = [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]
    
    # Sort both lists for comparison
    mst_edges_sorted = sorted(mst_edges)
    expected_edges_sorted = sorted(expected_edges)
    
    print(f"\nExpected edges: {expected_edges_sorted}")
    print(f"Actual edges:   {mst_edges_sorted}")
    
    assert mst_edges_sorted == expected_edges_sorted, f"Expected {expected_edges_sorted}, got {mst_edges_sorted}"
    
    
