"""
Background:
After picking a vertex, we update keys of adjacent vertices.

Task:
Implement a function to update key[] and parent[] for neighbors of selected vertex.

Instruction:
- Input: graph (adjacency matrix), u (selected vertex), key[], parent[], mstSet[]
- Update key[v] if edge weight is smaller.

Tip:
Skip vertices already in mstSet.

Test case:
graph = [
 [0, 2, 0],
 [2, 0, 3],
 [0, 3, 0]
]
u = 0
key = [0, ∞, ∞]
mstSet = [True, False, False]
parent = [-1, -1, -1]
# Expected after update:
# key = [0, 2, ∞]
# parent = [-1, 0, -1]
"""
def update_neighbors(graph, u, key, parent, mstSet):
    """
    Update key[] and parent[] arrays for neighbors of selected vertex u.
    
    Args:
        graph: Adjacency matrix representation of the graph
        u: Selected vertex (just added to MST)
        key: Array of key values for each vertex
        parent: Array of parent vertices in MST
        mstSet: Array indicating which vertices are in MST
    """
    V = len(graph)  # Number of vertices

    # Check all vertices
    for v in range(V):
        # Skip if:
        # 1. v is already in MST
        # 2. There's no edge from u to v (weight is 0)
        # 3. Current key[v] is already smaller than graph[u][v]
        if (not mstSet[v] and 
            graph[u][v] > 0 and 
            graph[u][v] < key[v]):

            # Update key and parent for vertex v
            key[v] = graph[u][v]
            parent[v] = u

# Test the function
if __name__ == "__main__":
    # Test case from the problem
    graph = [
        [0, 2, 0],
        [2, 0, 3],
        [0, 3, 0]
    ]
    u = 0
    key = [0, float('inf'), float('inf')]
    mstSet = [True, False, False]
    parent = [-1, -1, -1]

    print("Before update:")
    print(f"key = {key}")
    print(f"parent = {parent}")

    update_neighbors(graph, u, key, parent, mstSet)

    print("\nAfter update:")
    print(f"key = {key}")
    print(f"parent = {parent}")

    # Verify the expected results
    expected_key = [0, 2, float('inf')]
    expected_parent = [-1, 0, -1]

    assert key == expected_key, f"Expected key {expected_key}, got {key}"
    assert parent == expected_parent, f"Expected parent {expected_parent}, got {parent}"