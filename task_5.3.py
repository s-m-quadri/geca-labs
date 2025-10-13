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
def update_keys_and_parents(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        # Check if there's an edge from u to v, v is not in MST, and weight is less than current key[v]
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

    return key, parent

# Example usage
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

    updated_key, updated_parent = update_keys_and_parents(graph, u, key, parent, mstSet)
    print("Updated key:", updated_key)       # Expected: [0, 2, inf]
    print("Updated parent:", updated_parent) # Expected: [-1, 0, -1]