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

import math

def prim_iteration(graph, key, parent, mstSet):
    V = len(graph)

    # Step 1: Select min-key vertex not in MST
    min_key = math.inf
    u = -1
    for v in range(V):
        if not mstSet[v] and key[v] < min_key:
            min_key = key[v]
            u = v

    # Add selected vertex to MST
    mstSet[u] = True

    # Step 2: Update neighbors of u
    for v in range(V):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

    return key, parent, mstSet


# ---------- Test Case ----------
graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
key = [0, math.inf, math.inf]
mstSet = [True, False, False]
parent = [-1, -1, -1]

key, parent, mstSet = prim_iteration(graph, key, parent, mstSet)

print("key =", key)
print("parent =", parent)
print("mstSet =", mstSet)
