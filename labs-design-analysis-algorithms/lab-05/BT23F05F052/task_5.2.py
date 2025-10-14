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
def min_key(key, mstSet):
    mn = float('inf')
    idx = -1
    for i in range(len(key)):
        if not mstSet[i] and key[i] < mn:
            mn = key[i]
            idx = i
    return idx
