"""
Background:
Prim's algorithm builds MST by adding one vertex at a time.

Task:
Write a function to find the vertex with the minimum key not yet in MST.

Instruction:
- Input: key[], mstSet[]
- Output: index of minimum key vertex.

Tip:
Use a simple linear search.

Test case:
key = [0, 2, 3]
mstSet = [True, False, False]
# Expected output: 1
"""
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


key = [0, 2, 3]
mstSet = [True, False, False]
print(min_key_vertex(key, mstSet))