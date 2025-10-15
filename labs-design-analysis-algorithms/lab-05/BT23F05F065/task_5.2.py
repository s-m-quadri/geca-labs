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

def find_min_key_vertex(key, mstSet):
    """
    Find the vertex with minimum key value that is not yet in MST.
    
    Args:
        key: List of key values for each vertex
        mstSet: List indicating which vertices are in MST
    
    Returns:
        int: Index of the vertex with minimum key not in MST
    """
    min_value = float('inf')
    min_index = -1
    
    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_value:
            min_value = key[v]
            min_index = v
    
    return min_index


# Test case
if __name__ == "__main__":
    key = [0, 2, 3]
    mstSet = [True, False, False]
    
    result = find_min_key_vertex(key, mstSet)
    print(f"Minimum key vertex: {result}")
    print(f"Expected: 1")
    print(f"Test passed: {result == 1}")
