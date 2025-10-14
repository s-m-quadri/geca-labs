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
    Update key and parent arrays for neighbors of vertex u.
    
    Args:
        graph: Adjacency matrix representation of the graph
        u: The selected vertex
        key: List of key values
        parent: List of parent vertices
        mstSet: List indicating which vertices are in MST
    """
    V = len(graph)
    
    for v in range(V):
        # Update key[v] if:
        # 1. There is an edge from u to v (graph[u][v] != 0)
        # 2. v is not yet in MST (mstSet[v] == False)
        # 3. Weight of edge u-v is less than current key[v]
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u


# Test case
if __name__ == "__main__":
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
    
    print("\nExpected:")
    print(f"key = [0, 2, inf]")
    print(f"parent = [-1, 0, -1]")
    
    print(f"\nTest passed: {key == [0, 2, float('inf')] and parent == [-1, 0, -1]}")
