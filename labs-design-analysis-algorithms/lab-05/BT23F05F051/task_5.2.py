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
def minKey(key, mstSet):
    min_val = float('inf')
    min_index = -1

    for i in range(len(key)):
        # Pick the smallest key value from the vertices not yet included in MST
        if not mstSet[i] and key[i] < min_val:
            min_val = key[i]
            min_index = i

    return min_index

