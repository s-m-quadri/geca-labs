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

# solution:

import math

def min_key_vertex(key, mstSet):
    V = len(key)
    min_val = float('inf')
    min_index = -1
    for v in range(V):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index

def update_keys(graph, u, key, parent, mstSet):
    V = len(graph)
    for v in range(V):
        if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

def prim_iteration(graph, key, parent, mstSet):
    u = min_key_vertex(key, mstSet)
    mstSet[u] = True
    update_keys(graph, u, key, parent, mstSet)

graph = [
    [0, 1, 4],
    [1, 0, 2],
    [4, 2, 0]
]
V = len(graph)

key = [float('inf')] * V
parent = [-1] * V
mstSet = [False] * V

key[0] = 0

prim_iteration(graph, key, parent, mstSet)
prim_iteration(graph, key, parent, mstSet)

def display_list(lst):
    return ["∞" if (isinstance(x, float) and math.isinf(x)) else x for x in lst]

print("key    =", display_list(key))
print("parent =", parent)