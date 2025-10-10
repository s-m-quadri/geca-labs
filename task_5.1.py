"""
Background:
Prim's algorithm finds a Minimum Spanning Tree (MST) in a weighted graph.

Task:
Write a function that initializes key[], parent[], mstSet[] arrays for a graph with V vertices.

Instruction:
- Use Python lists.
- Do not implement the full MST yet.

Tip:
Focus only on initialization. Use ∞ for key values and -1 for parent.

Test case:
V = 4
# Expected:
# key = [∞, ∞, ∞, ∞]
# parent = [-1, -1, -1, -1]
# mstSet = [False, False, False, False]
"""
import sys
 
def prim_mst(graph):
    V = len(graph)             # Number of vertices
    key = [sys.maxsize] * V    # Initialize all keys as infinite
    parent = [-1] * V          # Array to store constructed MST
    key[0] = 0                 # Start from the first vertex
    mst_set = [False] * V      # To track vertices included in MST
 
    for _ in range(V):
        u = min((key[v], v) for v in range(V) if not mst_set[v])[1] # Pick min key vertex
        mst_set[u] = True # Include u in MST
 
        for v in range(V): # Update key and parent for neighbors of u
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u
 
    for i in range(1, V): # Print the constructed MST
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
 
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]
 
prim_mst(graph)
