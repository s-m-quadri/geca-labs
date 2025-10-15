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

def min_key_vertex(key, mstSet):
    min_value = float('inf')  # Initialize minimum value
    min_index = -1

    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v

    return min_index

# test case
key = [0, 2, 3]
mstSet = [True, False, False]
result = min_key_vertex(key, mstSet)
print("Index of minimum key vertex:", result)
