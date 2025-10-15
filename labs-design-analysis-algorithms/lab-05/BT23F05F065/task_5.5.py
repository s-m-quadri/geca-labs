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
    """Find vertex with minimum key value not yet in MST."""
    min_value = float('inf')
    min_index = -1
    
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v
    
    return min_index


def update_neighbors(graph, u, key, parent, mstSet):
    """Update key and parent arrays for neighbors of vertex u."""
    V = len(graph)
    
    for v in range(V):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u


def prim_mst(graph, start=0):
    """
    Implement Prim's algorithm to find MST.
    
    Args:
        graph: Adjacency matrix representation of the graph
        start: Starting vertex (default is 0)
    
    Returns:
        list: List of MST edges as tuples (parent, vertex, weight)
    """
    V = len(graph)
    
    # Initialize arrays
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    # Start from the given vertex
    key[start] = 0
    
    # MST will have V-1 edges
    mst_edges = []
    
    for _ in range(V):
        # Find vertex with minimum key not yet in MST
        u = find_min_key_vertex(key, mstSet)
        
        if u == -1:
            break
        
        # Add vertex to MST
        mstSet[u] = True
        
        # Add edge to MST (skip the starting vertex)
        if parent[u] != -1:
            mst_edges.append((parent[u], u, graph[parent[u]][u]))
        
        # Update keys and parents of adjacent vertices
        update_neighbors(graph, u, key, parent, mstSet)
    
    return mst_edges


# Test case
if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6],
        [2, 0, 3, 8],
        [0, 3, 0, 0],
        [6, 8, 0, 0]
    ]
    start = 0
    
    mst_edges = prim_mst(graph, start)
    
    print("MST edges (parent, vertex, weight):")
    for edge in mst_edges:
        print(f"  {edge}")
    
    print("\nExpected: [(0,1,2), (1,2,3), (0,3,6)]")
    
    total_weight = sum(edge[2] for edge in mst_edges)
    print(f"\nTotal MST weight: {total_weight}")
    print(f"Expected total weight: 11")
    
    print(f"\nTest passed: {total_weight == 11}")
