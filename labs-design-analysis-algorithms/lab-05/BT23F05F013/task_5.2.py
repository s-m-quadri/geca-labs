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
        mstSet: List of boolean values indicating if vertex is in MST
    
    Returns:
        int: Index of vertex with minimum key not in MST
    """
    min_key = float('inf')
    min_index = -1
    
    # Linear search through all vertices
    for v in range(len(key)):
        # Only consider vertices not yet in MST
        if not mstSet[v] and key[v] < min_key:
            min_key = key[v]
            min_index = v
    
    return min_index

# Test the function
if __name__ == "__main__":
    # Test case 1
    key = [0, 2, 3]
    mstSet = [True, False, False]
    result = find_min_key_vertex(key, mstSet)
    print(f"Test 1 - key: {key}, mstSet: {mstSet}")
    print(f"Min key vertex index: {result}")
    assert result == 1, f"Expected 1, got {result}"
    
    # Test case 2 - all vertices in MST
    key = [0, 2, 3]
    mstSet = [True, True, True]
    result = find_min_key_vertex(key, mstSet)
    print(f"\nTest 2 - key: {key}, mstSet: {mstSet}")
    print(f"Min key vertex index: {result}")
    assert result == -1, f"Expected -1, got {result}"
    
    # Test case 3 - multiple candidates
    key = [float('inf'), 5, 3, 7]
    mstSet = [True, False, False, False]
    result = find_min_key_vertex(key, mstSet)
    print(f"\nTest 3 - key: {key}, mstSet: {mstSet}")
    print(f"Min key vertex index: {result}")
    assert result == 2, f"Expected 2, got {result}"
    
    