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

def prim_iteration(graph, key, parent, mstSet):
    """
    Perform one iteration of Prim's algorithm.
    
    Args:
        graph: Adjacency matrix representation of the graph
        key: Array of key values for each vertex
        parent: Array of parent vertices in MST
        mstSet: Array indicating which vertices are in MST
    
    Returns:
        int: Index of the vertex added to MST in this iteration
    """
    # Step 1: Find the vertex with minimum key not yet in MST
    u = find_min_key_vertex(key, mstSet)

    # If no vertex found, MST is complete or graph is disconnected
    if u == -1:
        return -1

    # Step 2: Add the selected vertex to MST
    mstSet[u] = True

    # Step 3: Update keys of neighbors of the selected vertex
    update_neighbors(graph, u, key, parent, mstSet)

    return u

# Test the function
if __name__ == "__main__":
    # Test case from the problem - start fresh and show the progression
    graph = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]

    # Initialize arrays (vertex 0 is the starting point)
    key = [0, float('inf'), float('inf')]
    mstSet = [False, False, False]  # No vertices in MST initially
    parent = [-1, -1, -1]

    print("Initial state:")
    print(f"key = {key}")
    print(f"parent = {parent}")
    print(f"mstSet = {mstSet}")

    # First iteration: should select vertex 0 and update its neighbors
    selected_vertex = prim_iteration(graph, key, parent, mstSet)
    print(f"\nFirst iteration - Selected vertex: {selected_vertex}")
    print("After first iteration:")
    print(f"key = {key}")
    print(f"parent = {parent}")
    print(f"mstSet = {mstSet}")

    # Second iteration: should select vertex 1 (key=1) and update its neighbors
    selected_vertex = prim_iteration(graph, key, parent, mstSet)
    print(f"\nSecond iteration - Selected vertex: {selected_vertex}")
    print("After second iteration:")
    print(f"key = {key}")
    print(f"parent = {parent}")
    print(f"mstSet = {mstSet}")

    # Verify expected results match the problem's expected output
    expected_key = [0, 1, 2]
    expected_parent = [-1, 0, 1]

    assert key == expected_key, f"Expected key {expected_key}, got {key}"
    assert parent == expected_parent, f"Expected parent {expected_parent}, got {parent}"