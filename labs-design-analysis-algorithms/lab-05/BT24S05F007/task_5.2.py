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
def min_key_index(key, mstSet):
    """
    Return index of the minimum value in key[] among vertices not in mstSet.
    """
    min_val = float("inf")
    min_index = -1
    for i, k in enumerate(key):
        if not mstSet[i] and k < min_val:
            min_val = k
            min_index = i
    return min_index
