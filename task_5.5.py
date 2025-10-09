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
def minKey(key, mstSet):
    min_val = float('inf')
    min_index = -1
    for i in range(len(key)):
        if not mstSet[i] and key[i] < min_val:
            min_val = key[i]
            min_index = i
    return min_index


def primMST(graph, start=0):
    n = len(graph)
    
    key = [float('inf')] * n
    parent = [-1] * n
    mstSet = [False] * n

    key[start] = 0  # Start vertex

    for _ in range(n):
        # Step 1: Select min-key vertex not yet in MST
        u = minKey(key, mstSet)
        mstSet[u] = True

        # Step 2: Update ke
