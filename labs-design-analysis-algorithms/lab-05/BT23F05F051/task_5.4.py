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
def primMST(graph):
    n = len(graph)
    
    key = [float('inf')] * n      # Minimum weights to connect
    parent = [-1] * n             # To store MST
    mstSet = [False] * n          # Included vertices
    
    key[0] = 0  # Start from vertex 0

    for _ in range(n - 1):
        # Step 1: Pick min key vertex not in MST
        min_val = float('inf')
        u = -1
        for v in range(n):
            if not mstSet[v] and key[v] < min_val:
                min_val = key[v]
                u = v
        
        # Add vertex u to MST
        mstSet[u] = True
        
        # Step 2: Update keys and parents of neighbors
        for v in range(n):
            # graph[u][v] != 0 --> edge exists
            if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:

