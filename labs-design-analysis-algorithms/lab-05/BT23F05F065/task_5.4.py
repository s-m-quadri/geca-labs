"""
Background:
Prim's algorithm repeats selection and update steps to build MST.

Task:
Combine selection of min-key vertex and neighbor updates in one iteration.

Instruction:
- Implement one iteration of Prim's loop.
- Do not complete entire MST yet.

Tip:
Test on small 3-4 vertex graphs to check updates.

Test case:
graph = [
 [0, 1, 4],
 [1, 0, 2],
 [4, 2, 0]
]
key = [0, ∞, ∞]
mstSet = [True, False, False]
parent = [-1, -1, -1]
# Expected after iteration:
# key = [0, 1, 2]
# parent = [-1, 0, 1]
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


def prim_iteration(graph, key, parent, mstSet):
    """
    Perform one iteration of Prim's algorithm.
    
    Args:
        graph: Adjacency matrix
        key: List of key values
        parent: List of parent vertices
        mstSet: List indicating which vertices are in MST
    
    Returns:
        int: The vertex that was added to MST in this iteration
    """
    # Find the vertex with minimum key not yet in MST
    u = find_min_key_vertex(key, mstSet)
    
    if u == -1:
        return -1  # No more vertices to process
    
    # Add the vertex to MST
    mstSet[u] = True
    
    # Update keys and parents of adjacent vertices
    update_neighbors(graph, u, key, parent, mstSet)
    
    return u


# Test case
if __name__ == "__main__":
    graph = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]
    key = [0, float('inf'), float('inf')]
    mstSet = [True, False, False]
    parent = [-1, -1, -1]
    
    print("Before iteration:")
    print(f"key = {key}")
    print(f"parent = {parent}")
    print(f"mstSet = {mstSet}")
    
    vertex_added = prim_iteration(graph, key, parent, mstSet)
    
    print(f"\nVertex added to MST: {vertex_added}")
    print("\nAfter iteration:")
    print(f"key = {key}")
    print(f"parent = {parent}")
    print(f"mstSet = {mstSet}")
    
    print("\nExpected:")
    print(f"key = [0, 1, 2]")
    print(f"parent = [-1, 0, 1]")
    
    print(f"\nTest passed: {key == [0, 1, 2] and parent == [-1, 0, 1]}")
