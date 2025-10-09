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
def minKey(key, mstSet):
    min_val = float('inf')
    min_index = -1
    for i in range(len(key)):
        if not mstSet[i] and key[i] < min_val:
            min_val = key[i]
            min_index = i
    return min_index


def updateKeys(graph, u, key, parent, mstSet):
    n = len(graph)
    for v in range(n):
        # Update only if:
        # 1. Edge exists
        # 2. v not in MST
        # 3. Weight is smaller than current key[v]
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u


def primMST(graph):
    n = len(graph)
    
    key = [float('inf')] * n   # Minimum edge weight to include this vertex
    parent = [-1] * n          # To store MST structure
    mstSet = [False] * n       # True if vertex is included in MST
    
    # Start from vertex 0
    key[0] = 0
    
    for _ in range(n - 1):
        # Step 1: Pick minimum key vertex not yet in MST
        u = minKey(key, mstSet)
        mstSet[u] = True
        
        # Step 2: Update keys of neighbors of u
        updateKeys(graph, u, key, parent, mstSet)
    
    return parent, key


# ------------ TEST CASE ------------
graph = [
    [0, 2, 0],
    [2, 0, 3],
    [0, 3, 0]
]

parent, key = primMST(graph)

print("Parent:", parent)
print("Key:", key)
