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
def prim_mst(graph, start=0):
    V = len(graph)
    key = [float('inf')] * V       # Minimum weight to connect each vertex
    parent = [-1] * V              # Stores MST structure
    mstSet = [False] * V           # Track vertices included in MST

    key[start] = 0  # Start from given vertex

    for _ in range(V):
        # Step 1: Pick the vertex with minimum key not yet in MST
        u = -1
        min_value = float('inf')
        for i in range(V):
            if not mstSet[i] and key[i] < min_value:
                min_value = key[i]
                u = i

        mstSet[u] = True

        # Step 2: Update keys and parents for neighbors of u
        for v in range(V):
            if graph[u][v] > 0 and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Step 3: Build list of MST edges
    mst_edges = []
    for v in range(V):
        if parent[v] != -1:
            mst_edges.append((parent[v], v, graph[parent[v]][v]))

    return mst_edges

# Example usage
graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 0],
    [6, 8, 0, 0]
]

mst_edges = prim_mst(graph, start=0)
print("MST edges:", mst_edges)
